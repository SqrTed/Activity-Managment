from random import randint

from main.domain.Entities import Activity, Person


class Tests(object):
    def __init__(self, repo):
        self.__activityid = 1
        self.__contactid = 1
        self.__repo = repo

    months = (
        "march", "june", "july", "august", "september", "october", "november", "december", "january", "february")

    def __generate_contact_list(self):
        contacts = []
        n = randint(1, self.__contactid)
        for i in range(1, n + 1):
            x = randint(1, self.__contactid)
            if x not in contacts:
                contacts.append(x)
        return contacts

    @staticmethod
    def __generate_date(l):
        months = (
            "march", "june", "july", "august", "september", "october", "november", "december", "january", "february")
        while True:
            date = [randint(1, 31), months[randint(0, 9)], randint(2017, 2025)]
            if date[1] == "february":
                date[0] = randint(1, 28)
            ok = 1
            for x in l:
                if x.get_date() == date:
                    ok = 0
                    break
            if ok == 1:
                break
        return date[:]

    @staticmethod
    def __generate_time(l):
        while True:
            time = [randint(0, 23), randint(0, 59)]
            ok = 1
            for x in l:
                if x.get_time() == time:
                    ok = 0
                    break
            if ok == 1:
                break
        return time[:]

    @staticmethod
    def __generate_description():
        desc = ("footbal", "basketball", "painting", "airsoft", "math", "fundamentals of programing", "assembly",
                "computational logic", "algebra", "baseball", "voleyball", "cycling", "ski", "snowboarding", "skateing",
                "paintball", "party hard", "error debugging", "twerk", "music production")
        return desc[randint(0, 19)]

    def __generate_activity(self, i):
        activity_id = i
        contacts = self.__generate_contact_list()
        date = self.__generate_date(self.__repo.get_all())
        time = self.__generate_time(self.__repo.get_all())
        desc = self.__generate_description()
        return Activity(activity_id, contacts, date, time, desc)

    @staticmethod
    def __generate_name():
        name = (
            "Andrew Russell", "Lawrence Young", "Victor Alexander", "Evelyn Phillips", "Susan Barnes", "Carolyn Ross",
            "Nancy Adams", "Peter Bell", "George Williams", "Patrick Sanchez", "Ralph Ward", "Rebecca Henderson",
            "Christopher Hall", "Harold Stewart", "Charles Hughes", "Phillip Thomas", "Julie Price", "Kelly Ramirez",
            "Eugene Morris", "Gloria Edwards", "Bonnie Smith", "Donna Brown", "Paula Cox", "Kevin Jackson",
            "Gerald Nelson", "John Campbell", "Joe Green", "Steven Cook", "Richard Clark", "Doris Carter",
            "Beverly Hill", "Fred Parker", "Marie Peterson", "Frances Johnson", "Shirley Gonzalez", "Douglas Flores",
            "Theresa Washington", "Lois Kelly", "William Long", "Rachel Lee", "Daniel Gray", "Irene Scott",
            "Denise Gonzales", "Brandon Jenkins", "Sarah Patterson", "Roger Lewis", "Christina Baker", "Janice Jones",
            "Tina Watson", "Mircea Gabi")
        return name[randint(0, 49)]

    @staticmethod
    def __generate_phone():
        phone = 0
        for i in range(0, 9):
            phone *= 10
            phone += randint(0, 9)
        return phone

    @staticmethod
    def __generate_address():
        address = ("36 Shore Circle Abingdon, MD 21009", "9 Boston Drive Joliet, IL 6043585",
                   "Wentworth Court Kennewick, WA 99337",
                   "87 Garfield Street Port Charlotte, FL 33952", "8101 Saxton St. Pittsfield, MA 01201",
                   "78 Beacon Road Newark, NJ 07103",
                   "157 Ketch Harbour St.Winter Springs, FL 32708", "95 Addison Ave.Bloomington, IN 47401",
                   "242 Bridgeton Ave.Grandville, MI 49418", "8543 Foster Avenue Beckley, WV 25801",
                   "356 Grandrose Lane West Bend, WI 53095",
                   "9294 John Lane Fort Washington, MD 20744", "997 North Middle River St.Garland, TX 75043",
                   "292 Saxon Street Dearborn Heights, MI 48127", "7635 Ashley Drive Chillicothe, OH 45601",
                   "8996 Silver Spear Road Macomb, MI 48042", "3 E. Jones Court Morton Grove, IL 60053",
                   "9294 Wilson Rd.Selden, NY 11784", "3 Summit Dr.Somerset, NJ 08873",
                   "1 Brookside Dr.Cocoa, FL 32927")
        return address[randint(0, 19)]

    def __generate_contact(self, i):
        person_id = i
        name = self.__generate_name()
        phone = self.__generate_phone()
        address = self.__generate_address()
        return Person(person_id, name, phone, address)

    def generate(self, tip, test_id):
        if tip == "activity":
            self.__activityid = test_id
            return self.__generate_activity(test_id)
        elif tip == "contact":
            self.__contactid = test_id
            return self.__generate_contact(test_id)
