# Создайте класс и поля соответствующему вашему варианту (поля статические и динамические).
# Создайте три метода (класса, объекта и статический).
# Выберете поле или метод для реализации инкапсуляции.
# Пропишите запись и считывание (get, set) инкапсулированных полей.

# Вариант 3. Kласс House: id, Номер квартиры, Площадь, Этаж, Количество комнат, Улица, Тип здания, Срок эксплуатации.

import datetime


class House:
    # статические поля
    id = 0
    street = 'Gromova'

    # конструктор / динамические поля
    def __init__(self, square, floor, rooms_number, building_type, lifetime):
        self.square = square
        self.floor = floor
        self.rooms_number = rooms_number
        self.building_type = building_type
        self.lifetime = lifetime
        House.id += 1

    # метод класса
    @classmethod
    def set_house_id(cls):
        return cls.id

    # метод объекта / экземпляра класса
    def house_full_info(self):
        print(f"номер квартиры: {self.get_apartment_number()}, площадь: {self.square},"
              f"этаж: {self.floor}, количество комнат: {self.rooms_number}, улицв: {self.street},"
              f"срок эксплуатации до: {self.lifetime} года")

    # статический метод
    @staticmethod
    def lifetime_calc(lifetime):
        return lifetime - datetime.datetime.now().year

    # сеттер и геттер для инкапсулированного поля apartment_number

    def set_apartment_number(self, apartment_number):
        self.__apartment_number = apartment_number

    def get_apartment_number(self):
        return self.__apartment_number


# создание 2 объектов класса
first_house = House(67.8, 7, 2, 'houses', 2100)
first_house_id = House.set_house_id()   # использование метода класса
second_house = House(72.5, 8, 3, 'apartments', 2105)
second_house_id = House.set_house_id() # использование метода класса

# вывод всех динамических полей
print(first_house.__dict__)
print(second_house.__dict__)
print('-------------------------------------------------')

# вызов сеттеров для инкапсулированного поля, т.к. # print(first_house.id) или print(second_house.id) выдает ошибку
first_house.set_apartment_number('100')
House.set_apartment_number(second_house, '101')

# использование метода объекта / экземпляра класса
print('House', first_house_id)
first_house.house_full_info()
print('-------------------------------------------------')

print('House', second_house_id)
House.house_full_info(second_house)
print('-------------------------------------------------')

# использование статического метода
print(f'Количество оставшихся лет эксплуатации от текущего года по House {first_house_id}:', first_house.lifetime_calc(first_house.lifetime), 'лет')
print(f'Количество оставшихся лет эксплуатации от текущего года по House {second_house_id}:', second_house.lifetime_calc(second_house.lifetime), 'лет')
