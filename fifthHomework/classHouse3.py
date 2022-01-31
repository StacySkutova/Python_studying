# Функции-члены реализуют запись и считывание полей (проверка корректности),
# расчета возраста здания (необходимость в кап. ремонте).
# Создать список объектов.
# Вывести:
# a) список квартир, имеющих заданное число комнат;
# б) список квартир, имеющих заданное число комнат и расположенных на этаже, который находится в заданном промежутке;

import datetime


class House:
    houses_list = []

    # статические поля
    id = 0
    street = 'Gromova'

    # конструктор / динамические поля / магический метод
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

    def get_apartment_number(self):
        return self.__apartment_number

    # функции-члены реализуют запись и считывание полей (проверка корректности)
    # для инкапсулированного поля
    def set_apartment_number(self, apartment_number):
        if apartment_number > 0:
            self.__apartment_number = apartment_number
        else:
            print("Номер квартиры не может быть отрицательным или нулевым!")

    # для открытого поля
    def set_square(self, square):
        if square > 0:
            self.square = square
        else:
            print("Площадь не может быть отрицательной или нулевой!")

    # метод для расчета возраста здания (необходимость в кап. ремонте): предположим, что необходимость возникает по окончании эксплуатационного срока

    def overhaul_needed(self):
        rest_time = self.lifetime - datetime.datetime.today().year;
        print('До необходимости капитального ремонта осталось', rest_time, 'лет')

    # метод для вывода списка квартир, имеющих заданное число комнат + магический метод

    def get_room_list(self, rooms_number_sorted):
        new_house_list = []
        i = 0
        while i < len(self.houses_list):
            if self.houses_list.__getitem__(i).rooms_number == rooms_number_sorted:
                new_house_list.append(self.houses_list.__getitem__(i))
            i += 1
        return new_house_list

    # метод для изменения представления экземпляра класса / магический метод

    def __repr__(self):
        return '(%r, %r, %r, %r, %r)' % (self.square, self.floor, self.rooms_number, self.building_type, self.lifetime)

    # метод для вывода списка квартир, имеющих заданное число комнат и расположенных на этаже, который находится в заданном промежутке + магический метод

    def get_room_and_floor(self, rooms_number_sorted, floor_min, floor_max):
        new_house_list = []
        i = 0
        while i < len(self.houses_list):
            if (self.houses_list.__getitem__(i).rooms_number == rooms_number_sorted) and (self.houses_list.__getitem__(i).floor > floor_min and self.houses_list.__getitem__(i).floor < floor_max):
                new_house_list.append(self.houses_list.__getitem__(i))
            i += 1
        return new_house_list


# создание 2 объектов класса
first_house = House(67.8, 7, 2, 'houses', 2100)
second_house = House(72.5, 8, 3, 'apartments', 2105)

# создание 10 объектов класса
House.houses_list = [House(67.8, 7, 2, 'houses', 2100), House(72.5, 8, 3, 'apartments', 2105), House(70.5, 9, 3, 'apartments', 2102), House(77.2, 8, 3, 'apartments', 2103), House(101.6, 6, 4, 'houses', 2110), House(67.8, 7, 2, 'houses', 2100), House(95.8, 5, 4, 'houses', 2095), House(81.3, 7, 3, 'houses', 2101), House(69.8, 8, 2, 'apartments', 2075), House(84.3, 9, 2, 'apartments', 2081)]


# вспомогательные методы/для наведения красоты при выводе информации + магический метод
def print_list_defined_rooms(class_name, param_sorted):
    i = 0
    list_required = House.get_room_list(class_name, param_sorted)
    while i < len(list_required):
        print(i+1, ') ', list_required.__getitem__(i))
        i += 1


def print_list_defined_rooms_and_floor(class_name, param_sorted, param_min, param_max):
    i = 0
    list_required = House.get_room_and_floor(class_name, param_sorted, param_min, param_max)
    while i < len(list_required):
        print(i+1, ') ', list_required.__getitem__(i))
        i += 1


# реализация методов
print('Анализ необходимости капитального ремонта')
first_house.overhaul_needed();
second_house.overhaul_needed();
print('-------------------------------------------------')

print('Cписок квартир, имеющих заданное число комнат:\n')
print_list_defined_rooms(House, 3)
print('-------------------------------------------------')

print('Cписок квартир, имеющих заданное число комнат и расположенных на этаже, который находится в заданном промежутке\n')
print_list_defined_rooms_and_floor(House, 2, 5, 10)
print('-------------------------------------------------')