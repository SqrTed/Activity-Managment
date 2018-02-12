class UndoOperation(object):
    def __init__(self, source_method, handler, args_1, args_2):
        self.__source_method = source_method
        self.__handler = handler
        self.__args_1 = args_1
        self.__args_2 = args_2

    @property
    def source_method(self):
        return self.__source_method

    @property
    def handler(self):
        return self.__handler

    @property
    def args_1(self):
        return self.__args_1

    @property
    def args_2(self):
        return self.__args_2


class UndoRedoManager(object):
    def __init__(self):
        self.__operations = []
        self.__redo = []

    def register(self, source_method, handler, args_1, args_2):
        """
        :param source_method:
        :param handler:
        :param args:
        :return:
        """
        self.__operations.append(UndoOperation(source_method, handler, args_1, args_2))

    @property
    def get_operations(self):
        return len(self.__operations)

    @property
    def get_redo(self):
        return len(self.__redo)

    def reset_redo(self):
        self.__redo.clear()

    def undo(self):
        operation = self.__operations.pop()
        operation.handler(operation.args_1)
        self.__redo.append(UndoOperation(operation.handler, operation.source_method, operation.args_2, operation.args_1))

    def redo(self):
        redo = self.__redo.pop()
        redo.handler(redo.args_1)
