class Table:

    count = 0
    # Способ создания объекта (конструктор)
    def __init__(self, width, height):
        self.width = width
        self.height = height
        Table.count += 1

    def getWidth(self):   # Метод для вывода свойвства в print
        return self.width

    def getHeight(self):
        return self.height

    # Метод расчета площади.
    def getArea(self):
        return self.width * self.height

    @staticmethod
    def meters_to_feet(area_in_meters):
        return area_in_meters * 10.764

    @classmethod
    def print_tables_counter(cls):
        print(f"Tables: {cls.count}")


# Создаем 2 объекта: r1 & r2
t1 = Table(10, 5)
Table.print_tables_counter()
t2 = Table(20, 11)
Table.print_tables_counter()

print("t1.width = ", t1.width)
print("t1.height = ", t1.height)
print("t1.getWidth() = ", t1.getWidth())
print("t1.getArea() = ", t1.getArea())

print("-----------------")

print("t2.width = ", t2.width)
print("t2.height = ", t2.height)
print("t2.getWidth() = ", t2.getWidth())
print("t2.getArea() = ", t2.getArea())
print("t2.getArea() in feet = ", Table.meters_to_feet(t2.getArea()))


# журнальный стол
class JournalTable(Table):
    storage = 0


# обеденный стол
class DinnerTable(Table):
    places = 0

    def __init__(self, width, height=0):
        Table.__init__(self, width, height)
        self.places = width//5

    def getPlaces(self):
        return self.places


t3 = DinnerTable(10)
Table.print_tables_counter()
print(t3.getPlaces())