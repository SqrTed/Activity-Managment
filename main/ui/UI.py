from main.domain.Entities import Activity, Person
from main.validation.Validator import ManagementException


class Command:
    """
    Built for an easier calling of the ui functions
    """

    def __init__(self, cmd_id, cmd_function, cmd_text):
        self.cmdID = cmd_id
        self.__cmdFunction = cmd_function
        self.cmdText = cmd_text

    def execute(self):
        self.__cmdFunction()


class UI:
    """
    The class takes care of the UI
    """

    def __init__(self, activity_service, contact_service, statistics_service, undo_redo_manager):
        self.__activity_service = activity_service
        self.__contact_service = contact_service
        self.__statistics_service = statistics_service
        self.__undo_redo_manager = undo_redo_manager

    @staticmethod
    def __print_menu(commands):
        """
        Prints the menu or submenus based on the commands
        :param commands:
        :return:
        """
        print("Activity management:")
        for cmd in commands.values():
            print(cmd.cmdText)

    @staticmethod
    def __read_cmd():
        """
        reads the command
        :return: an integer number
        """
        return int(input(">>"))

    @staticmethod
    def __input_contact():
        """
        Reads the details of a contact
        :return: a list containing the contact details
        """
        return Person(int(input("Person's Id: ")), input("Name: "), int(input("Phone number: +40")), input("Address: "))

    def __ui_add_contact(self):
        """
        Adds the contact to the contact repository
        :return:
        """
        person = self.__input_contact()
        self.__contact_service.add(person)

    @staticmethod
    def __input_activity():
        """
        Reads the details of an activity
        :return: returns a list containing the details of the activity
        """
        activity = [int(input("Activity Id: ")), list(map(int, input("Participant's Id's: ").split()))]
        date = input("Date: ").split()
        date[0] = int(date[0])
        date[1] = int(date[2])
        activity.append(date)
        activity.append(list(map(int, input("Time: ").split())))
        activity.append(input("Description: "))
        return Activity(*activity)

    def __ui_add_activity(self):
        """
        Adds the activity to the activity repository
        :return:
        """
        activity = self.__input_activity()
        self.__activity_service.add(activity)

    def __to_add(self):
        """
        Prints the submenu of adding elements to the application and calls the suitable functions for adding them
        :return:
        """
        add = {1: Command(1, self.__ui_add_contact, "\t1. Add contact"),
               2: Command(2, self.__ui_add_activity, "\t2. Add activity"),
               0: Command(0, "default", "\t0. We have to go back!")}
        self.__print_menu(add)
        try:
            command = self.__read_cmd()
            if command == 0:
                return
            if command in add:
                self.__undo_redo_manager.reset_redo()
                add[command].execute()
            print("Successfully added!\n")
        except ValueError:
            print("Error: Must input a number!!!\n")

    def __ui_remove_contact(self):
        """
        Removes a contact based on it's Id
        :return:
        """
        person_id = int(input("Insert the Id of the element: "))
        self.__contact_service.remove(Person(person_id, "Default", 1234, "Default"))

    def __ui_remove_activity(self):
        """
        Removes an activity based on it's Id
        :return:
        """
        activity_id = int(input("Insert the Id of the element: "))
        self.__activity_service.remove(Activity(activity_id, [1], [1, "january", 0], [0, 0], "Default"))

    def __to_remove(self):
        """
        Takes care of printing the menu for removing an element from the applications and calls the suitable methods
        :return:
        """
        remove = {1: Command(1, self.__ui_remove_contact, "\t1. Remove contact"),
                  2: Command(2, self.__ui_remove_activity, "\t2. Remove activity"),
                  0: Command(0, "default", "\t0. We have to go back!")}
        self.__print_menu(remove)
        try:
            command = self.__read_cmd()
            if command == 0:
                return
            if command in remove:
                self.__undo_redo_manager.reset_redo()
                remove[command].execute()
            print("Successfully removed!\n")
        except ValueError:
            print("Error: Must input a number!!!\n")

    def __ui_update_contact(self):
        """
        Updates a contact based on the info the user introduces. The Id must already be in the application to work
        :return:
        """
        person = self.__input_contact()
        self.__contact_service.update(person)

    def __ui_update_activity(self):
        """
        Updates an activity based on the info the user introduces. The Id must already be in the application to work
        :return:
        """
        activity = self.__input_activity()
        self.__activity_service.update(activity)

    def __to_update(self):
        """
        Takes care of printing the submenu for updating elements in the application and calls the suitable methods
        :return:
        """
        update = {1: Command(1, self.__ui_update_contact, "\t1. Update contact"),
                  2: Command(2, self.__ui_update_activity, "\t2. Update activity"),
                  0: Command(0, "default", "\t0. We have to go back!")}
        self.__print_menu(update)
        try:
            command = self.__read_cmd()
            if command == 0:
                return
            if command in update:
                self.__undo_redo_manager.reset_redo()
                update[command].execute()
            print("Successfully Updated!")
        except ValueError:
            print("Error: Must input a number!!!\n")

    def __to_list(self):
        """
        Takes care of printing the submenu for listing the elements of the app and calls the suitable methods
        :return:
        """
        to_print = {1: Command(1, self.__to_list, "\t1. List contacts"),
                    2: Command(2, self.__to_list, "\t2. List activities"),
                    0: Command(0, "default", "\t0. We have to go back!")}
        self.__print_menu(to_print)
        try:
            command = self.__read_cmd()
            if command == 0:
                return
            if command in to_print:
                if command == 1:
                    print(self.__contact_service.list_all())
                else:
                    print(self.__activity_service.list_all())
        except ValueError:
            print("Must input a number!!!")

    def __ui_find_contact(self):
        """
        Finds a contact in the contact repository based on a given name or phone number.
        :return: Prints the list of all matching items
        """
        found = self.__contact_service.find(input("Insert name or phone number: "))
        if len(found) != 0:
            for item in found:
                print(item)
            return
        print("\nCouldn't find any matching contact...\n")

    def __ui_find_activity(self):
        """
        Finds an activity in the activity repository based on a given date, time and description
        :return: Prints the list of all matching items
        """
        found = self.__activity_service.find(input("Insert date,time or description: ").split())
        if len(found) != 0:
            for item in found:
                print(item)
            return
        print("\nCouldn't find any matching activity...\n")

    def __to_find(self):
        """
        Prints the submenu and calls the appropriate methods for finding elements in the application
        :return:
        """
        find = {1: Command(1, self.__ui_find_contact, "\t1. Find contact"),
                2: Command(2, self.__ui_find_activity, "\t2. Find activity"),
                0: Command(0, "default", "\t0. We have to go back!")}
        self.__print_menu(find)
        try:
            command = self.__read_cmd()
            if command == 0:
                return
            if command in find:
                find[command].execute()
        except ValueError:
            print("Error: Must input a number!!!\n")

    def add_tests(self, test):
        """
        Adds automatically generated tests
        :param test:
        :return:
        """
        if len(test) == 4:
            self.__contact_service.add(test)
            # self.__backup.append((self.__contactservice.remove, [contact[0]]))
        elif len(test) == 5:
            self.__activity_service.add(test)
            # self.__backup.append((self.__activityservice.remove, [activity[0]]))

    def __ui_sort_by_day(self):
        """
        Sorts the activities by a given day
        :return:
        """
        found = self.__statistics_service.sort_by_day(int(input("\tInsert day: ")))
        print("\n")
        for item in found:
            print(item)
        print("\n")

    def __ui_busiest_days(self):
        """
        Prints the list of upcoming days with activities, sorted in descending order of the number of
        activities in each day
        :return:
        """
        found = self.__statistics_service.busiest_days()
        for item in found:
            for it in item.activities:
                print(it)
        print("\n")

    def __ui_with_person(self):
        """
        Prints the activities with a given person
        :return:
        """
        found = self.__contact_service.find(input("Insert name: "))
        if len(found) != 0:
            print("Contacts found: \n")
            for item in found:
                print(item)
            found = self.__statistics_service.with_person(
                int(input("Please insert the Id of the contact you want to check: ")))
            print("\n")
            print(found)
            for item in found:
                print(item)
            return
        print("\nCouldn't find any matching contact...\n")

    def __ui_sort_by_activity_number(self):
        """
        List all persons in the address book, sorted in descending order of the number of upcoming activities to
        which they will participate.
        :return:
        """
        found = self.__statistics_service.sort_by_activities_number()
        for item in found:
            print("Participating in: " + str(item[1].total) + " activities\n" + str(item[1].person))
        return

    def __to_stats(self):
        """
        Takes care of printing the submenu for statistics and calls suitable methods
        :return:
        """
        stats = {1: Command(1, self.__ui_sort_by_day, "\t1. List the activities for a given day"),
                 2: Command(2, self.__ui_busiest_days, "\t2. Busiest days"),
                 3: Command(3, self.__ui_with_person, "\t3. List activities with a given person"),
                 4: Command(4, self.__ui_sort_by_activity_number,
                            "\t4. List all persons sorted by the number of activities"),
                 0: Command(0, "default", "\t0. We have to go back!")}
        self.__print_menu(stats)
        try:
            command = self.__read_cmd()
            if command == 0:
                return
            if command in stats:
                stats[command].execute()
        except ValueError:
            print("Error: Must input a number!!!\n")

    def __to_undo(self):
        """
        Checks if an undo operation is possible.
        If it is calls the method responsible of doing the undo
        Otherwise prints a message
        :return:
        """
        if self.__undo_redo_manager.get_operations != 0:
            self.__undo_redo_manager.undo()
            print("\nSuccessfully undone last operation!\n")
        else:
            print("\nNothing to be done!\n")

    def __to_redo(self):
        """
        Checks if a redo operation is possible.
        If it is calls the method responsible of doing the redo
        Otherwise prints a message
        :return:
        """
        if self.__undo_redo_manager.get_redo != 0:
            self.__undo_redo_manager.redo()
            print("\nSuccessfully redone last operation!\n")
        else:
            print("\nNothing to be done!\n")

    def run_ui(self):
        """
        Takes care of printing the menu, processing the commands and executing the matching commands.
        Most of the commands point to submenus which take care of specified tasks
        :return:
        """
        commands = {1: Command(1, self.__to_add, "1. Add..."), 2: Command(2, self.__to_update, "2. Update..."),
                    3: Command(3, self.__to_remove, "3. Remove..."), 4: Command(4, self.__to_list, "4. List..."),
                    5: Command(5, self.__to_find, "5. Find..."), 6: Command(6, self.__to_stats, "6. Statistics..."),
                    7: Command(7, self.__to_undo, "7. Undo"), 8: Command(8, self.__to_redo, "8. Redo"),
                    0: Command(0, "default", "0. Exit")
                    }
        while True:
            self.__print_menu(commands)
            try:
                cmd = self.__read_cmd()
                if cmd == 0:
                    return
                elif cmd in commands:
                    try:
                        commands[cmd].execute()
                    except ManagementException as ME:
                        print(ME)
                    except ValueError:
                        print("Invalid types!!!\n")
                else:
                    print("Invalid command!!!\n")
            except ValueError:
                print("Must input a number!!!\n")
