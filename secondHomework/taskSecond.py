# Задачи на многомерные списки
# Вариант 1: в матрице найти номер строки,
# сумма чисел в которой максимальна.

import numpy as np

print("Введите желаемое количество строк в матрице")
row = int(input())
print("Введите желаемое количество колонок в матрице")
column = int(input())
array = np.random.sample((row, column))
print("Рандомная матрица по полученному числу строк и колонок \n", array)

sumRow = array.sum(axis=1)
print("Сумма значений каждой строки", sumRow)

maxNumber = np.argmax(sumRow)
print("Индекс строки, сумма чисел в которой максимальна -", maxNumber)
