import unittest


def make_squares(a, b, n=0):
    if a == b:
        print("Сторона", n+1, "квадрата равна ", a)
        return n + 1   # и так уже квадрат, а мы режем прямоугольник на квадраты
    if a < b:
        print("Сторона", n+1, "квадрата равна ", a)
        return make_squares(a, b - a, n + 1)  # рекурсия - сама себя, но иные аргументы
    print("Сторона", n+1, "квадрата равна ", b)
    return make_squares(a - b, b, n + 1)   # рекурсия - сама себя, но иные аргументы


class RecursionTest(unittest.TestCase):
    def test_recursion(self):
        self.assertEqual(make_squares(12, 10), 6)


if __name__ == '__main__':
    unittest.main()
