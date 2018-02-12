from main.domain.Entities import *
from main.validation.Validator import ManagementException


class RepositoryException(ManagementException):
    pass


class MyList(object):
    def __init__(self):
        self.__elements = []
        self.__index = 0

    def append(self, element):
        self.__elements.append(element)

    def __getitem__(self, item):
        for element in self.__elements:
            if element.get_id() == item.get_id():
                return element

    def __setitem__(self, key, value):
        for i in range(1, len(self.__elements)):
            if self.__elements[i].get_id() == key.get_id():
                self.__elements[i] = value
                return

    def __delitem__(self, key):
        index = -1
        for i in range(1, len(self.__elements)):
            if self.__elements[i].get_id() == key.get_id():
                index = i
                break
        if index != -1:
            del self.__elements[index]

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index >= len(self.__elements):
            self.__index = 0
            raise StopIteration
        element = self.__elements[self.__index]
        self.__index += 1
        return element

    def all(self):
        return self.__elements[:]

    def filter(self, f):
        return [x for x in self.__elements if f(x)]

    @staticmethod
    def __comb_sort(l, f):
        gap = len(l)
        swaps = True
        while gap > 1 or swaps:
            gap = max(1, int(gap / 1.25))  # minimum gap is 1
            swaps = False
            for i in range(len(l) - gap):
                j = i + gap
                if f(l[i], l[j]):
                    l[i], l[j] = l[j], l[i]
                    swaps = True
        return l

    def sort(self, f):
        self.__elements = self.__comb_sort(self.__elements, f)
        return self.__elements[:]

    def __str__(self):
        to_print = ""
        for elem in self.__elements:
            to_print += str(elem) + '\n'
        return to_print

    def __len__(self):
        return len(self.__elements)


class Repository(object):
    def __init__(self):
        self.__elements = MyList()

    def add(self, elem):
        if elem in self.__elements.all():
            raise RepositoryException("Error!!! Please insert a valid element!!!")
        elif isinstance(elem, Activity):
            for element in self.__elements:
                if elem.comp(element):
                    raise RepositoryException("Error!!! Please insert a valid date and time!!!")
        self.__elements.append(elem)

    def remove(self, elem):
        if elem not in self.__elements.all():
            raise RepositoryException("Error!!! Element could not be found!!!")
        del self.__elements[elem]

    def update(self, elem):
        if elem not in self.__elements.all():
            raise RepositoryException("Error!!! Please insert a valid element!!!")
        elif isinstance(elem, Activity):
            for element in self.__elements:
                if elem.comp(element) and elem != element:
                    raise RepositoryException("Error!!! Please insert a valid date and time!!!")
        self.__elements[elem] = elem

    def find(self, element):
        return self.__elements[element]

    def __str__(self):
        return str(self.__elements)

    def get_all(self):
        return self.__elements.all()

    def sort(self, func):
        return self.__elements.sort(func)

    def filter(self, func):
        return self.__elements.filter(func)
