import unittest
from pythonProject.fourthHomework import classHouse3


class HouseTest(unittest.TestCase):
    def setUp(self):
        """Set up for separated test"""
        print("Set up for [" + self.shortDescription() + "]")

    def tearDown(self):
        """Tear down for separated test"""
        print("Tear down for [" + self.shortDescription() + "]")

    def test_lifetime_calc(self):
        """Lifetime_calc method test"""
        self.assertEqual(78, classHouse3.first_house.lifetime_calc(2100))

    def test_get_apartment_number(self):
        """Get_apartment_number method test"""
        self.assertGreater(classHouse3.second_house.get_apartment_number(), classHouse3.first_house.get_apartment_number())

    def test_house_full_info(self):
        """House_full_info method test"""
        self.assertMultiLineEqual("Gromova", classHouse3.House.street.__str__())


if __name__ == '__main__':
    unittest.main()
