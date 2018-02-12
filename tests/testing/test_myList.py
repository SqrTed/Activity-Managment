from unittest import TestCase

from main.repository.Repository import MyList


class TestMyList(TestCase):
    def setUp(self):
        self.__list = MyList()

    def test_append(self):
        self.__list.append(1)
        self.assertTrue(len(self.__list) == 1)

    def test_all(self):
        self.__list.append(1)
        self.assertEqual(self.__list.all(), [1])

    def test_filter(self):
        self.__list.append(1)
        self.__list.append(2)
        self.__list.append(3)
        self.__list.filter(lambda x: x > 2)
        self.assertEqual(self.__list.all(), [3])

    def test_sort(self):
        self.__list.append(11)
        self.__list.append(2)
        self.__list.append(31)
        self.__list.sort(lambda x, y: x > y)
        self.assertEqual(self.__list.all(), [2, 11, 31])
