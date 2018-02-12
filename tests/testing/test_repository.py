from unittest import TestCase

from main.domain.Entities import Person, Activity
from main.repository.Repository import Repository, RepositoryException


class TestRepository(TestCase):
    def setUp(self):
        self.__person_1 = Person(1, "Name", 1234, "Address")
        self.__person_2 = Person(2, "Name", 5678, "Address2")
        self.__activity_1 = Activity(1, [7, 8], [1, "January", 2017], [0, 10], "Default Description")
        self.__activity_2 = Activity(2, [9, 10], [1, "January", 2017], [0, 10], "Default")
        self.__activity_3 = Activity(3, [9, 10], [1, "January", 2017], [0, 0], "Default")
        self.__repo = Repository()

    def test_add_person(self):
        pass

    def test_add_activity(self):
        self.__repo.add(self.__activity_1)
        with self.assertRaises(RepositoryException):
            self.__repo.add(self.__activity_1)
        with self.assertRaises(RepositoryException):
            self.__repo.add(self.__activity_2)

    def test_remove(self):
        self.__repo.add(self.__activity_1)
        with self.assertRaises(RepositoryException):
            self.__repo.remove(self.__activity_2)
        self.__repo.remove(self.__activity_1)

    def test_update(self):
        self.__repo.add(self.__activity_1)
        with self.assertRaises(RepositoryException):
            self.__repo.update(self.__activity_3)
        self.__repo.add(self.__activity_3)
        with self.assertRaises(RepositoryException):
            self.__repo.update(Activity(1, [9, 10], [1, "January", 2017], [0, 0], "Default"))
        self.__repo.update(self.__activity_1)

    def test_find(self):
        self.__repo.add(self.__activity_1)
        self.assertTrue(self.__repo.find(self.__activity_1) == self.__activity_1)

    def test_get_all(self):
        self.__repo.add(self.__activity_1)
        self.__repo.add(self.__activity_3)
        self.assertTrue(self.__repo.get_all() == [self.__activity_1, self.__activity_3])

    def test_str(self):
        self.__repo.add(self.__activity_1)
        self.assertEqual(str(self.__repo),
                         "Activity Id: 1\nPersons Id's: 7 8 \nDate: 1 January 2017\nTime: 0:10\nDescription: Default Description\n\n")
