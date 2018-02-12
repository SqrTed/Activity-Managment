import os
from main.repository.Repository import Repository
from main.service.Backup_Service import UndoRedoManager
from main.service.Service import ActivityService, ContactService, StatisticService
from main.ui.UI import UI
from tests.generating_tests.Tests import Tests
from main.repository.TextFile import File
from main.repository.BinaryFile import BinaryFile
from main.domain.Entities import Person, Activity


def tests(ui, repo):
    """
    Auto-generating tests
    :param ui:
    :param repo:
    :return:
    """
    generate_test = Tests(repo)
    for i in range(0, 50):
        ui.add_tests(generate_test.generate("contact", i + 1))
    for i in range(0, 100):
        ui.add_tests(generate_test.generate("activity", i + 1))


class StartApp(object):
    def __init__(self):
        self.__console = UI
        self.load_settings()

    def load_settings(self):
        path = os.path.join(os.path.join(os.path.dirname(__file__), 'settings'), 'properties')
        file = open(path, "r")
        line = file.readline().strip().split(" = ")
        text = line[1].strip('"')
        if text == "inmemory":
            self.__run_inmemory()
        if text == "textfile":
            contacts = file.readline().strip().split(" = ")
            contacts = contacts[1].strip('"')
            activities = file.readline().strip().split(" = ")
            activities = activities[1].strip('"')
            self.__run_textfile(contacts, activities)
        if text == "binaryfile":
            contacts = file.readline().strip().split(" = ")
            contacts = contacts[1].strip('"')
            activities = file.readline().strip().split(" = ")
            activities = activities[1].strip('"')
            self.__run_binaryfile(contacts, activities)
        file.close()

    def __run_binaryfile(self, contacts, activities):
        """
        The repository uses binary files
        :return:
        """
        activity_repository = BinaryFile(activities)
        contacts_repository = BinaryFile(contacts)
        undo_redo_manager = UndoRedoManager()
        activity_service = ActivityService(activity_repository, undo_redo_manager)
        contact_service = ContactService(contacts_repository, undo_redo_manager)
        statistics_service = StatisticService(activity_repository, contacts_repository)
        self.__console = UI(activity_service, contact_service, statistics_service, undo_redo_manager)
        # tests(self.__console, activity_repository)

    def __run_textfile(self, contacts, activities):
        """
        The repository uses text files
        :return:
        """
        activity_repository = File(activities, Activity)
        contacts_repository = File(contacts, Person)
        undo_redo_manager = UndoRedoManager()
        activity_service = ActivityService(activity_repository, undo_redo_manager)
        contact_service = ContactService(contacts_repository, undo_redo_manager)
        statistics_service = StatisticService(activity_repository, contacts_repository)
        self.__console = UI(activity_service, contact_service, statistics_service, undo_redo_manager)
        # tests(self.__console, activity_repository)

    def __run_inmemory(self):
        """
        The repository is in memory
        :return:
        """
        activity_repository = Repository()
        contacts_repository = Repository()
        undo_redo_manager = UndoRedoManager()
        activity_service = ActivityService(activity_repository, undo_redo_manager)
        contact_service = ContactService(contacts_repository, undo_redo_manager)
        statistics_service = StatisticService(activity_repository, contacts_repository)
        self.__console = UI(activity_service, contact_service, statistics_service, undo_redo_manager)
        tests(self.__console, activity_repository)

    def run(self):
        self.__console.run_ui()


def startup():
    """
    Starting the application
    :return:
    """
    try:
        app = StartApp()
        app.run()
    except FileNotFoundError:
        print("Error!!! Couldn't find any matching files in .../main/repository/files")


startup()
