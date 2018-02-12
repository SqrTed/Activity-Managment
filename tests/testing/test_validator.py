from unittest import TestCase

from main.domain.Entities import Activity, Person
from main.validation.Validator import ValidatorException, Validator


class TestValidator(TestCase):
    def setUp(self):
        self.__validator = Validator

    def test_validate_activity(self):
        with self.assertRaises(ValidatorException):
            self.__validator.validate_activity(Activity(-1, [1, 2, 3], [1, "january", 2017], [0, 0], "Default"))
        with self.assertRaises(ValidatorException):
            self.__validator.validate_activity(Activity(1, [1, 2, 3], [1, "default", 2017], [0, 0], "Default"))
        with self.assertRaises(ValidatorException):
            self.__validator.validate_activity(Activity(1, [1, 2, 3], [34, "january", 2017], [0, 0], "Default"))
        with self.assertRaises(ValidatorException):
            self.__validator.validate_activity(Activity(1, [1, 2, 3], [0, "january", 2017], [0, 0], "Default"))
        with self.assertRaises(ValidatorException):
            self.__validator.validate_activity(Activity(1, [1, 2, 3], [31, "february", 2017], [0, 0], "Default"))
        with self.assertRaises(ValidatorException):
            self.__validator.validate_activity(Activity(1, [1, 2, 3], [1, "january", 2016], [0, 0], "Default"))
        with self.assertRaises(ValidatorException):
            self.__validator.validate_activity(Activity(1, [1, 2, 3], [1, "january", 2017], [0, 0], "123"))
        with self.assertRaises(ValidatorException):
            self.__validator.validate_activity(Activity(1, [1, 2, 3], [0, "january", 2017], [-1, 0], "Default"))
        with self.assertRaises(ValidatorException):
            self.__validator.validate_activity(Activity(1, [1, 2, 3], [0, "january", 2017], [25, 0], "Default"))
        with self.assertRaises(ValidatorException):
            self.__validator.validate_activity(Activity(1, [1, 2, 3], [0, "january", 2017], [0, -1], "Default"))
        with self.assertRaises(ValidatorException):
            self.__validator.validate_activity(Activity(1, [1, 2, 3], [0, "january", 2017], [0, 60], "Default"))

    def test_validate_person(self):
        with self.assertRaises(ValidatorException):
            self.__validator.validate_person(Person(-1, "Name", 123, "Address"))
        with self.assertRaises(ValidatorException):
            self.__validator.validate_person(Person(1, "123", 123, "Address"))
        with self.assertRaises(ValidatorException):
            self.__validator.validate_person(Person(1, "Name", -1, "Address"))
        with self.assertRaises(ValidatorException):
            self.__validator.validate_person(Person(1, "Name", 123, "67123"))
