city_num = int(input()) #taking number of city from user
heroes = 0
heroes_level = ''

for city in range(1,city_num + 1):
    heroes = int(input()) #taking number of heroes from user
    heroes_level = input()
    heroes_list = []
    for each_hero in heroes_level.split():
        heroes_list.append(int(each_hero))
    
    hero_set = set(heroes_list)
    if 0 in heroes_list:
        print(len(heroes_list) - heroes_list.count(0))
    elif len(hero_set) != len(heroes_list):
        print(len(heroes_list))
    else:
        print(len(heroes_list) + 1)
        
    
    