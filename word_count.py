# -*- coding: utf-8 -*-
import io, re
'''Эта функция совершает подсчет слов возвращет список слов и их количество'''
#filename ='ProjectGutenberg.txt' # для теста
#filename ='test_words.txt'
def lower_words(filename):
    try:
        with io.open(filename, encoding='utf-8', errors='ignore') as gutnberg_obj:#
        #with open (filename,encoding='utf-8') as gutnberg_obj:
            contents = gutnberg_obj.read()
    except FileNotFoundError:
        msg = 'Файл ' + filename + 'отсутствует'
        print(msg)
    else:
        # Удаление лишних символов регулярным выражением
        words_lower = contents.lower()# с маленькой буквы
        words = re.findall(r'\w+', words_lower)  #  регулярка
        #words = contents.lower().split()
        # Подсчет слов, примерный
        num_words = len(words)
        print('В тексте файла '+ filename + ' ' + str(num_words) +' слов.')
        return(words,num_words)# возвращает список слов с маленькой буквы / количество слов
        
#w,n = lower_words(filename) #для теста
#print(w)