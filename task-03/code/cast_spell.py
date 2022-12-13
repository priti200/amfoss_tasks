s = input()
spell_word_count, words_count = s.split()
spell_word_count = int(spell_word_count)
int(spell_word_count)
words_count = int(words_count)

word_dict = {}

for i in range(words_count):
    translation_words = input()
    first_word,second_word = translation_words.split()
    if len(first_word) < len(second_word):
        first_word,second_word = second_word,first_word
        word_dict[first_word] = second_word
        
    elif len(first_word) == len(second_word):
        word_dict[second_word] = first_word
        
    else:
        word_dict[first_word] = second_word
        
_spell = input()
spell_lst = []
spell_lst =_spell.split()

for _count,_word in enumerate(spell_lst,start=0):
    if spell_lst[_count] in word_dict:
        spell_lst[_count]=word_dict[_word]

final_spell = ""
for j in spell_lst:
    final_spell = final_spell + j +' '
    
print(final_spell)