from unittest import TestCase

from main.domain.Entities import Activity, Dta


class TestDta(TestCase):
    def setUp(self):
        self.__activity_1 = Activity(1, [1, 2, 3], [1, "January", 2017], [0, 0], "Default")
        self.__activity_2 = Activity(1, [4, 5, 6], [1, "January", 2017], [0, 1], "Description")
        self.__activity_3 = Activity(2, [9, 10], [3, "January", 2017], [0, 20], "Default")
        self.__dta = Dta([1, "January", 2017], self.__activity_1)

    def test_date(self):
        self.assertEqual(self.__dta.date, [1, "January", 2017])

    def test_activities(self):
        self.assertEqual(len(self.__dta.activities), 1)

    def test_add_activity(self):
        self.assertEqual(len(self.__dta.activities), 1)
        self.__dta.add_activity(self.__activity_2)
        self.assertEqual(len(self.__dta.activities), 2)

    def test_equal(self):
        self.assertFalse(self.__dta == self.__activity_3)
        self.assertFalse(self.__dta == Dta([3, "January", 2017],self.__activity_3))
