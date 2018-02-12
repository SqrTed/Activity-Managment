from unittest import TestCase

from main.domain.Entities import Person


class TestPerson(TestCase):
    def setUp(self):
        self.__person = Person(1, "Name", 1234, "Address")

    def test_get_id(self):
        self.assertEqual(self.__person.get_id(), 1)

    def test_get_name(self):
        self.assertEqual(self.__person.get_name(), "Name")

    def test_get_phone(self):
        self.assertEqual(self.__person.get_phone(), 1234)

    def test_get_address(self):
        self.assertEqual(self.__person.get_address(), "Address")

    def test_update(self):
        self.__person.update(Person(2, "Second Name", 5678, "Second Address"))
        self.assertEqual(self.__person.get_name(), "Second Name")
        self.assertEqual(self.__person.get_phone(), 5678)
        self.assertEqual(self.__person.get_address(), "Second Address")
        self.assertTrue(self.__person.get_id() == 1)

    def test_find(self):
        self.assertTrue(self.__person.find("Na") != -1)
        self.assertTrue(self.__person.find(12) != -1)

    def test_str(self):
        self.assertEqual(str(self.__person), "Id: 1\nName: Name\nPhone: +401234\nAddress: Address\n")

    def test_len(self):
        self.assertEqual(len(self.__person), 4)

    def test_eq(self):
        person = Person(2, "Name", 1234, "Address")
        self.assertFalse(self.__person == person)
        number = 3
        self.assertFalse(self.__person == number)
