import pickle
import os

from main.repository.Repository import Repository
from main.repository.Repository import RepositoryException


class BinaryException(RepositoryException):
    pass


class BinaryFile(Repository):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = os.path.join(os.path.join(os.path.dirname(__file__), 'files'), file_name)
        self.__read_file()

    def __read_file(self):
        with open(self.__file_name, 'rb') as file:
            try:
                while True:
                    super().add(pickle.load(file))
            except EOFError:
                pass

    def __write_file(self):
        try:
            file = open(self.__file_name, "wb")
            elements = Repository.get_all(self)
            for element in elements:
                pickle.dump(element, file)
            file.close()
        except IOError as error:
            raise BinaryException("Error!!!" + str(error))

    def add(self, elem):
        super().add(elem)
        self.__write_file()

    def remove(self, elem):
        super().remove(elem)
        self.__write_file()

    def update(self, elem):
        super().update(elem)
        self.__write_file()

    def find(self, element):
        return super().find(element)

    def get_all(self):
        return super().get_all()

    def __str__(self):
        to_print = ""
        for element in super().get_all():
            to_print += str(element) + '\n'
        return to_print
