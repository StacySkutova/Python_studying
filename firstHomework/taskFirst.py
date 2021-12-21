# Даны 3 числа a, b и c. Найти среднее геометрическое этих чисел, если все они отличны от нуля,
# и среднее арифметическое в противном случае.

from math import sqrt
a = float(input('a='))
b = float(input('b='))
c = float(input('c='))
if a != 0 and b != 0 and c != 0:
    geometricMean = (a+b+c)**0.33
    print("Среднее геометрическое a, b, c, отличных от 0: " + str(geometricMean))
else:
    average = (a + b + c) / 3
    print("Среднее арифметическое a, b, c при иных обстоятельсвах (есть 0): " + str(average))