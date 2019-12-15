# -*- coding: utf-8 -*-
'''
Закон Ципфа
Программа для вывода гистограммы по эмпирической закономерности распределения частоты слов естественного языка:
если все слова языка (или просто достаточно длинного текста) упорядочить по убыванию частоты их использования,
 то частота n-го слова в таком списке окажется приблизительно обратно пропорциональной его порядковому номеру n 
 (так называемому рангу этого слова, см. шкала порядка). Например, второе по используемости слово встречается 
 примерно в два раза реже, чем первое, третье — в три раза реже, чем первое, и так далее.
'''
import matplotlib.pyplot as plt
import json
from word_count import lower_words
'''Тут происходит подсчет повторений слов
   в идеале нужно освоить matplotlib и вывести гистограмму'''

filename ='ProjectGutenberg.txt'#'ProjectGutenberg.txt' 'test_words.txt'
# получение списка слов и кол-ва слов в тексте
low_words, num_words = lower_words(filename)
word_data = {} 
#Цикл посчитывает кол-во вхождений, а потом удаляет повторения слова и так далее
for word in low_words:
    word_data[word] = low_words.count(word)
    try:
        while True:
            low_words.remove(word)
    except ValueError:
        pass
# Сложим словарь в БД Json
filename = 'wordsdata.json'
with open(filename,'w', encoding ='utf-8') as f_obj: #конструкция открытия файла в переменной f_obj (w режим записи)
    json.dump(word_data, f_obj, ensure_ascii=False) # dump - сохраняемые данные|объект для получения
    
# Упрощенная гисторамма(для больших данных не подходит),  надо изучить настройки и сортировать данные
#plt.bar(list(word_data.keys()), sorted(word_data.values(),reverse=True), color='g') # попытка сортировки приводит к запутыванию
#plt.show()
'''
Моя гистограмма работает неправильно, так как словарь{} не сортируется, а задача показать убывание количества с
увеличением позиции.
отсортировать значения оказалось плохой идеей потому что они перепутываются относительно ключей
Поэтому далее преобразовываем словарь в список кортежей.
код пример:
>>> d = { 'a': 1, 'b': 2, 'c': 3 }
>>> d.items()
[('a', 1), ('c', 3), ('b', 2)]
>>> [(v, k) for k, v in d.items()]
[(1, 'a'), (3, 'c'), (2, 'b')]
Сортировка по выбранной позиции!? ,с параметром реверса:
sorted(student_tuples, key=itemgetter(2), reverse=True)
'''
clean_data = word_data.items() # ненужная команда
iterdata = [(v,k) for k,v in word_data.items()]# создание списка кортежей с конф-ей:[(кол-во э.,элемент),(кол-во э.,элемент)]
plotdata=(sorted (iterdata, reverse=True)) # такую структуру легко отсортировать,доп параметр реверс
# С помощью циклов Создаём два списка для библиотеки plt,для вывода:
k=[]
v=[]
for i in plotdata:
    k.append(i[0]) # список кол-ва повторений по y-координате
for j in plotdata:
    v.append(j[1]) # v - список слов по x-координате
x_values = list(range(1,len(v)+1)) # генерируем список что бы заменить слова
x_values = [str(x) for x in x_values] # делаем из цифр букавы(str)

#вывод на экран гистограммы:
plt.xticks(rotation=90) # поворот на 90 гр слов по оси X
plt.tick_params(axis='y', which='both', labelsize=8, pad=1) # параметры отступа и шрифта

plt.bar(v[0:int(len(v)*0.06)],k[0:int(len(v)*0.06)],color='b') # Используем не весь славарь, а срез 6% значений
#plt.bar(x_values[0:int(len(v)*0.06)],k[0:int(len(v)*0.06)],color='b')
plt.title('Закон Ципфа в действии!\n', fontsize = 16)
plt.xlabel('Слова в тексте по популярности', fontsize=16)
plt.ylabel('Количество повторений слов', fontsize = 14)
plt.show()
# Вычислим отношения кол-ва к наибольшему кол-ву
ratio = [] 
j=1
for i in k[1:]:
    ratio.append(k[0]/i)
x_ratioval = list(range(2,len(ratio)+1)) # Значения отношений по Х

plt.figure(dpi=128,facecolor= 'silver', figsize=(7, 5))
plt.plot(x_ratioval[0:30], ratio[0:30], c = 'purple',linewidth=2, alpha=1)# линии
# Заголовки
plt.title('График отношения к наибольшему повторению', fontsize = 14)
plt.xlabel('Номер по убыванию от большего', fontsize=11)
plt.ylabel('Отношение к наибольшему', fontsize = 11)

plt.tick_params(axis='both', which='major', labelsize=10, pad=4)
#plt.tick_params(axis='both', which='minor', labelsize=20)

axes = plt.gca()
# axes.set_xlim([xmin,xmax])
#axes.set_ylim([0,2])

plt.show()