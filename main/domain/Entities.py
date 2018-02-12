from random import randint


class Activity(object):
    def __init__(self, activity_id, person_ids, date, time, desc):
        self.__activity_id = activity_id
        self.__personIds = person_ids
        self.__date = date
        self.__time = time
        self.__desc = desc

    def get_id(self):
        return self.__activity_id

    def get_date(self):
        return self.__date

    def get_persons(self):
        return self.__personIds

    def get_time(self):
        return self.__time

    def get_description(self):
        return self.__desc

    def update(self, item):
        self.__desc = item.get_description()
        self.__time = item.get_time()
        self.__personIds = item.get_persons()
        self.__date = item.get_date()

    def __str__(self):
        to_print = "Activity Id: "
        to_print += str(self.__activity_id) + "\nPersons Id's: "
        for person_id in self.__personIds:
            to_print += str(person_id) + " "
        to_print += "\nDate: " + str(self.__date[0]) + " " + self.__date[1] + " " + str(
            self.__date[2]) + "\nTime: " + str(self.__time[0]) + ":" + str(
            self.__time[1]) + "\nDescription: " + self.__desc + "\n"
        return to_print

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__activity_id == other.__activity_id

    def comp(self, other):
        if isinstance(other, self.__class__):
            if self.__activity_id == other.__activity_id:
                return True
            elif self.__date == other.__date and self.__time == other.__time:
                return True
        return False

    def __len__(self):
        return 5


class Person(object):
    def __init__(self, person_id, name, phone, address):
        self.__personId = person_id
        self.__name = name
        self.__phone = phone
        self.__address = address

    def get_id(self):
        return self.__personId

    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

    def get_address(self):
        return self.__address

    def update(self, item):
        self.__name = item.get_name()
        self.__phone = item.get_phone()
        self.__address = item.get_address()

    def __len__(self):
        return 4

    def __str__(self):
        return "Id: " + str(self.__personId) + "\nName: " + self.__name + "\nPhone: +40" + str(
            self.__phone) + "\nAddress: " + self.__address + '\n'

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__personId == other.__personId
        else:
            return False

    def find(self, args):
        if str(args).isdigit():
            args = str(args)
            return str(self.__phone).find(args)
        else:
            return self.__name.find(args)


class Dto(object):
    def __init__(self, person):
        self.__person = person
        self.__total = 1

    @property
    def person(self):
        return self.__person

    def set_person(self, value):
        self.__person = value

    @property
    def total(self):
        return self.__total

    def increase(self):
        self.__total += 1


class Dta(object):
    def __init__(self, date, activity):
        self.__activities = []
        self.__activities.append(activity)
        self.__date = date

    @property
    def date(self):
        return self.__date

    @property
    def activities(self):
        return self.__activities

    def add_activity(self, value):
        self.__activities.append(value)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.date == self.__date
        else:
            return False