from unittest import TestCase

from main.domain.Entities import Person, Dto


class TestDto(TestCase):
    def setUp(self):
        self.__person = Person(2, "Name_2", 12345, "Address_2")
        self.__dto = Dto(Person(1, "Name", 1234, "Address"))

    def test_person_setter(self):
        self.__dto.set_person(self.__person)
        self.assertEqual(self.__dto.person, self.__person)
        self.assertEqual(self.__dto.person.get_name(), self.__person.get_name())
        self.assertEqual(self.__dto.person.get_phone(), self.__person.get_phone())
        self.assertEqual(self.__dto.person.get_address(), self.__person.get_address())

    def test_person_getter(self):
        self.assertEqual(self.__dto.person.get_id(), 1)
        self.assertEqual(self.__dto.person.get_name(), "Name")
        self.assertEqual(self.__dto.person.get_phone(), 1234)
        self.assertEqual(self.__dto.person.get_address(), "Address")

    def test_total(self):
        self.assertEqual(self.__dto.total, 1)

    def test_increase(self):
        self.__dto.increase()
        self.assertEqual(self.__dto.total, 2)
