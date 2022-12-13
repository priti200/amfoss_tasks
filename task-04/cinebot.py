import os
import telebot
import requests
import json
import csv, io

yourkey = "4f242392"
bot_id = "5776279686:AAH7gaaVq33HqCIBCFFio3BiZAp-OtssCMI"

bot = telebot.TeleBot(bot_id)

s = io.StringIO()
buf = io.BytesIO()


@bot.message_handler(commands=['start','hello'])
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(message, 'Hello there! I am a bot that will show  movie information for you and export it in a csv file.\n\n' )

@bot.message_handler(commands=['stop','bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message,'Bye!\nHave a good time')

@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    bot.reply_to(message,'1.0 You can use \"/movie MOVIE_NAME\" command to get the details of a particular movie. For eg: \"/movie The Shawshank Redemption\"\n\n2.0. You can use \"/export\" command to export all the movie data in CSV format.\n\n3.0. You can use \"/stop\" or the command \"/bye\" to stop the bot.')

@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):
    movieName = message.text.replace('/movie ', "")
    bot.reply_to(message,'Getting movie info...')
    api_url = f"http://www.omdbapi.com/?apikey={yourkey}&t={movieName}"
    movieDetails = requests.get(api_url).json()
    moviePoster = movieDetails['Poster']
    movieTitle = movieDetails['Title']
    movieYear = movieDetails['Year']
    movieRating = movieDetails['Rated']

    bot.reply_to(message,'/movie')

    csv.writer(s).writerow([movieTitle,movieYear,movieRating])
    s.seek(0)

    buf.write(s.getvalue().encode())
    buf.seek(0)

    buf.name = f'datas.csv'
    
    bot.send_photo(message.chat.id, moviePoster , f'Title: {movieTitle} \nReleased_Year: {movieYear}\nRating: {movieRating}')


@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
   bot.reply_to(message,'Generating the data file')
   bot.send_document(message.chat.id,buf) 
   

@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand '+'\N{confused face}')

bot.infinity_polling()