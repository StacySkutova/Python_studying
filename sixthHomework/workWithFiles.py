# В соответствии со своим вариантом разработать программу для работы с файлами на языке Python.
# Предварительно создать текстовый файл F1 не менее чем из 10 строк и записать в него информацию.

# Вариант 5
# Скопировать из файла F1 в файл F2 строки, начиная с четвертой по порядку.
# Подсчитать количество символов в последнем слове F2.

# запись всех строк из F1 в F2
file_in = open('F1.txt', 'r')
file_out = open('F2.txt', 'w')
file_out.write(file_in.read())

# запись 4ой строки из F1 в F2
with open('F1.txt', 'r') as f:
    for i in range(3):
        f.readline()
    x = f.readline()
file_out = open('F2.txt', 'w')
file_out.write(x)

# запись начиная с 4ой строки из F1 в F2
with open('F1.txt') as file:
    lines = file.readlines()
lines = ''.join(lines[3:])
file_out = open('F2.txt', 'w')
file_out.write(lines)