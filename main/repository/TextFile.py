from main.domain.Entities import Person, Activity
from main.repository.Repository import Repository, RepositoryException
import os


class FileException(RepositoryException):
    pass


class File(Repository):
    def __init__(self, file_name, tip):
        super().__init__()
        self.__file_name = os.path.join(os.path.join(os.path.dirname(__file__), 'files'), file_name)
        self.__tip = tip
        self.__read_file()

    def __read_file(self):
        file = open(self.__file_name, "r")
        line = file.readline()
        while line:
            line = line.strip('\n').split(";")
            if self.__tip == Person:
                super().add(Person(int(line[0]), line[1], int(line[2]), line[3]))
            elif self.__tip == Activity:
                date = line[2].split()
                date[0] = int(date[0])
                date[2] = int(date[2])
                time = line[3].split()
                super().add(Activity(int(line[0]), list(map(int, line[1].split())), date, list(map(int, time)),
                                     line[4]))
            line = file.readline()
        file.close()

    def __write_to_file(self):
        if self.__tip == Person:
            self.__write_persons()
        elif self.__tip == Activity:
            self.__write_activities()

    def __write_persons(self):
        try:
            file = open(self.__file_name, "w")
            persons = super().get_all()
            for person in persons:
                to_write = str(person.get_id()) + ";" + str(person.get_name()) + ";" + str(
                    person.get_phone()) + ";" + str(
                    person.get_address()) + '\n'
                file.write(to_write)
            file.close()
        except IOError as error:
            raise FileException("Error!!! " + str(error))

    def __write_activities(self):
        try:
            file = open(self.__file_name, "w")
            activities = super().get_all()
            for activity in activities:
                to_write = str(activity.get_id()) + ";"
                for person_id in activity.get_persons():
                    to_write += str(person_id)
                    to_write += " "
                to_write += ";" + str(
                    activity.get_date()[0]) + " " + activity.get_date()[1] + " " + str(
                    activity.get_date()[2]) + ";" + str(
                    activity.get_time()[0]) + " " + str(activity.get_time()[1]) + ";" + str(
                    activity.get_description()) + '\n'
                file.write(to_write)
            file.close()
        except IOError as error:
            raise FileException("Error!!! " + str(error))

    def add(self, elem):
        super().add(elem)
        self.__write_to_file()

    def remove(self, elem):
        super().remove(elem)
        self.__write_to_file()

    def update(self, elem):
        super().update(elem)
        self.__write_to_file()

    def find(self, element):
        return super().find(element)

    def __str__(self):
        to_print = ""
        for element in super().get_all():
            to_print += str(element) + '\n'
        return to_print

    def get_all(self):
        return super().get_all()
