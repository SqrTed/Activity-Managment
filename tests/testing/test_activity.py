from unittest import TestCase

from main.domain.Entities import Activity


class TestActivity(TestCase):
    def setUp(self):
        self.__activity = Activity(1, [1, 2, 3], [1, "January", 2017], [0, 0], "Default")

    def test_get_id(self):
        self.assertEqual(self.__activity.get_id(), 1)

    def test_get_date(self):
        self.assertEqual(self.__activity.get_date(), [1, "January", 2017])

    def test_get_persons(self):
        self.assertEqual(self.__activity.get_persons(), [1, 2, 3])

    def test_get_time(self):
        self.assertEqual(self.__activity.get_time(), [0, 0])

    def test_get_description(self):
        self.assertEqual(self.__activity.get_description(), "Default")

    def test_update(self):
        self.__activity.update(Activity(1, [4, 5, 6], [2, "January", 2017], [0, 1], "Description"))
        self.assertEqual(self.__activity.get_id(), 1)
        self.assertEqual(self.__activity.get_date(), [2, "January", 2017])
        self.assertEqual(self.__activity.get_persons(), [4, 5, 6])
        self.assertEqual(self.__activity.get_time(), [0, 1])
        self.assertEqual(self.__activity.get_description(), "Description")

    def test_comp(self):
        activity_1 = Activity(1, [7, 8], [3, "January", 2017], [0, 10], "Default Description")
        activity_2 = Activity(2, [9, 10], [1, "January", 2017], [0, 0], "Default")
        activity_3 = Activity(2, [9, 10], [1, "January", 2017], [0, 20], "Default")
        self.assertTrue(self.__activity.comp(activity_1))
        self.assertTrue(self.__activity.comp(activity_2))
        self.assertFalse(self.__activity.comp(activity_3))

    def test_equal(self):
        activity_1 = Activity(1, [7, 8], [3, "January", 2017], [0, 10], "Default Description")
        activity_2 = Activity(2, [9, 10], [1, "January", 2017], [0, 0], "Default")
        self.assertFalse(activity_1 == activity_2)

    def test_str(self):
        activity = Activity(1, [1], [3, "January", 2017], [0, 10], "Default")
        self.assertEqual(str(activity),
                         "Activity Id: 1\nPersons Id's: 1 \nDate: 3 January 2017\nTime: 0:10\nDescription: Default\n")

    def test_len(self):
        activity = Activity(1, [1], [3, "January", 2017], [0, 10], "Default")
        self.assertEqual(len(activity), 5)
