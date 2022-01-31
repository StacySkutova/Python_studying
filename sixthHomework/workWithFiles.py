# В соответствии со своим вариантом разработать программу для работы с файлами на языке Python.
# Предварительно создать текстовый файл F1 не менее чем из 10 строк и записать в него информацию.

# Вариант 5
# Скопировать из файла F1 в файл F2 строки, начиная с четвертой по порядку.
# Подсчитать количество символов в последнем слове F2.

import codecs

# запись всех строк из F1 в F2
file_in = open('F1.txt', 'r')
file_out = open('F2.txt', 'w')
file_out.write(file_in.read())

# запись только 4ой строки из F1 в F2
with open('F1.txt', 'r') as file_in:
    for i in range(3):
        file_in.readline()
    line = file_in.readline()
file_out = open('F2.txt', 'w')
file_out.write(line)

# запись начиная с 4ой строки из F1 в F2
with open('F1.txt') as file_in:
    line = file_in.readlines()
lines = ''.join(line[3:])
file_out = open('F2.txt', 'w')
file_out.write(lines)

# подсчет количества символов в последнем слове F2
file_in = codecs.open('F2.txt', 'r', 'utf-8')
last_line = file_in.readlines()[-1]
last_word = last_line.split()[-1]
symbol_count = len(last_word)
print('Последняя строка в файле F2:', last_line)
print('Последнее слово в файле F2:', last_word)
print('Количество символов в последнем слове в файле F2:', symbol_count)

