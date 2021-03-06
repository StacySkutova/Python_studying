# Реализуйте рекурсивную функцию нарезания прямоугольника с заданными пользователем сторонами a и b
# на квадраты с наибольшей возможной на каждом этапе стороной.
# Выведите длины ребер получаемых квадратов и кол-во полученных квадратов.

width = int(input("Длина:  "))
height = int(input("Ширина: "))


def make_squares(a, b, n=0):
    if a == b:
        print("Сторона", n+1, "квадрата равна ", a)
        return n + 1   # и так уже квадрат, а мы режем прямоугольник на квадраты
    if a < b:
        print("Сторона", n+1, "квадрата равна ", a)
        return make_squares(a, b - a, n + 1)  # рекурсия - сама себя, но иные аргументы
    print("Сторона", n+1, "квадрата равна ", b)
    return make_squares(a - b, b, n + 1)   # рекурсия - сама себя, но иные аргументы


print("Количество возможных квадратов из заданного прямоугольника равно ", make_squares(width, height))


