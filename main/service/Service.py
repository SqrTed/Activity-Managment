from main.domain.Entities import *
from main.validation.Validator import Validator


class ActivityService(object):
    """
    The controller/service with the operations/functions need to be applied on the activity repository
    """

    def __init__(self, activities_repository, undo_manager):
        self.__activities = activities_repository
        self.__undo_manager = undo_manager
        self.__validator = Validator()

    def add(self, activity):
        """
        Adds an activity to the repository if valid, otherwise pops errors
        :param activity:
        :return:
        """
        self.__validator.validate_activity(activity)
        self.__activities.add(activity)
        self.__undo_manager.register(self.add, self.remove, activity, activity)

    def remove(self, activity):
        """
        Removes an activity if it is in the repository, otherwise pops errors
        :param activity:
        :return:
        """
        self.__validator.validate_activity(activity)
        activity = self.__activities.find(activity)
        self.__activities.remove(activity)
        self.__undo_manager.register(self.remove, self.add, activity, activity)

    def update(self, activity):
        """
        Updates an activity if it is in the repository, otherwise pops errors
        :param activity:
        :return:
        """
        self.__validator.validate_activity(activity)
        second_activity = self.__activities.find(activity)
        self.__activities.update(activity)
        self.__undo_manager.register(self.update, self.update, second_activity, activity)

    def list_all(self):
        """
        Lists all activities
        :return:
        """
        return self.__activities

    def __find_time(self, args):
        """
        :param args:
        :return: a filtered list with all the elements matching a given time(args) (partial matching also)
        """
        return list(
            filter(lambda x: x.get_time()[0] == args[0] or x.get_time()[1] == args[1], self.__activities.get_all()))

    def __find_date(self, args):
        """
        :param args:
        :return: a filtered list with all the elements matching a given date(args) (partial matching also)
        """
        return list(
            filter(lambda x: x.get_date()[0] == args[0] or x.get_date()[1] == args[1] or x.get_date()[2] == args[2],
                   self.__activities.get_all()))

    def __find_desc(self, args):
        """
        :param args:
        :return: a filtered list with all the elements that match a given description(args) (partial matching also)
        """
        return list(filter(lambda x: x.get_description().find(args) != -1, self.__activities.get_all()))

    def find(self, args):
        """
        Evaluates the input and calls the appropriate function for matching/finding/searching
        :param args:
        :return:
        """
        months = (
            "march", "june", "july", "august", "september", "october", "november", "december", "january", "february")
        if len(args) == 2 and args[1].isdigit() and args[0].isdigit():
            args = list(map(int, args))
            activity = Activity(1, [1], [1, "january", 0], [args[0], args[1]], "Default")
            self.__validator.validate_activity(activity)
            return self.__find_time(args)
        elif len(args) == 3 and args[1] in months:
            activity = Activity(1, [1], [int(args[0]), args[1], int(args[2])], [12, 00], "Default")
            self.__validator.validate_activity(activity)
            args = [int(args[0]), args[1], int(args[2])]
            return self.__find_date(args)
        else:
            args = " ".join(args)
            return self.__find_desc(args)


class ContactService(object):
    """
    The controller/service with the operations/functions need to be applied on the contacts repository
    """

    def __init__(self, contacts_repository, undo_manager):
        self.__contacts = contacts_repository
        self.__validator = Validator()
        self.__undo_manager = undo_manager

    def add(self, person):
        """
        Adds a contact to the repository if valid, otherwise pops errors
        :param person:
        :return:
        """
        self.__validator.validate_person(person)
        self.__contacts.add(person)
        self.__undo_manager.register(self.add, self.remove, person, person)

    def remove(self, person):
        """
        Removes a contact from the repository if the given id is in repository, otherwise pops errors
        :param person:
        :return:
        """
        self.__validator.validate_person(person)
        person = self.__contacts.find(person)
        self.__contacts.remove(person)
        self.__undo_manager.register(self.remove, self.add, person, person)

    def update(self, person):
        """
        Updates a contact from the repository if the given id is in repository and the information is valid,
        otherwise pops errors
        :param person:
        :return:
        """
        self.__validator.validate_person(person)
        second_person = self.__contacts.find(person)
        self.__contacts.update(person)
        self.__undo_manager.register(self.update, self.update, second_person, person)

    def list_all(self):
        """
        Lists all contacts in the repository
        :return:
        """
        return self.__contacts

    def find(self, args):
        """
        Evaluates the args to match the cases in which finding a contact is applicable(phone number/name)
        :param args:
        :return: a filtered list matching the args(partial matching also)
        """
        if args.isdigit():
            return list(filter(lambda x: str(x.get_phone()).find(args) != -1, self.__contacts.get_all()))
        else:
            return list(filter(lambda x: x.get_name().find(args) != -1, self.__contacts.get_all()))


class StatisticService(object):
    """
    The controller/service with the operations/functions need to be applied on the both repositories
    """

    def __init__(self, activities_repo, contacts_repo):
        self.__activities = activities_repo
        self.__contacts = contacts_repo

    def busiest_days(self):
        """
        Returns a list of upcoming days with activities, sorted in descending order of the number of
        activities in each day
        :return:
        """
        activities = self.__activities.get_all()
        busiest = []
        for act in activities:
            dt = Dta(act.get_date(), act)
            if dt in busiest:
                busiest[busiest.index(dt)].add_activity(act)
            else:
                busiest.append(dt)
        return sorted(busiest, key=lambda x: len(x.activities), reverse=True)

    def with_person(self, person_id):
        """
        :param person_id:
        :return: a filtered list with all the activities containing the person described by the id
        """
        # return list(filter(lambda x: person_id in x.get_persons(), self.__activities.get_all()))
        return self.__activities.filter(lambda x: person_id in x.get_persons())

    def sort_by_activities_number(self):
        """
        :return:the list of all persons in the address book, sorted in descending order of the number of
        upcoming activities to which they will participate
        """
        found = {}
        activities = self.__activities.get_all()
        for act in activities:
            for person in act.get_persons():
                if person not in found.keys():
                    found.update({person: Dto(self.__contacts.find(Person(person, "Default", 0, "Default")))})
                else:
                    found[person].increase()
        return sorted(found.items(), key=lambda x: x[1].total, reverse=True)

    def sort_by_day(self, day):
        """
        Prints the list of upcoming days with activities, sorted in descending order of the number of
        activities in each day
        :param day:
        :return:
        """

        def less_than(act1, act2):
            if act1.get_time() == act2.get_time():
                return act1.get_date() < act1.get_date()
            return act1.get_time() < act2.get_time()

        Activity.__lt__ = less_than

        # _list = filter(lambda x: x.get_date()[0] == day, self.__activities.get_all())
        _list = self.__activities.filter(lambda x: x.get_date()[0] == day)
        _list = sorted(_list)

        Activity.__lt__ = object.__lt__

        return _list


"""
s = Repository()
a = Repository()
service = ManagementService(a, s)
service.addActivity(1, [1, 2, 3, 4, 5, 6], [24, "september", 2017], [22,30], "gaming night")
service.addActivity(2, [1, 2, 3, 4, 5, 6], [25, "september", 2017], [22,30], "gaming night")
service.listActivities()
service.removeActivity(1)
service.listActivities()
"""
