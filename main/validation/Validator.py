class ManagementException(Exception):
    pass


class ValidatorException(ManagementException):
    pass


class Validator(object):
    @staticmethod
    def validate_activity(activity):
        errors = ""
        months = (
            "march", "june", "july", "august", "september", "october", "november", "december", "january", "february")
        if activity.get_id() < 0:
            errors += "Invalid ID!!!\n"
        if activity.get_date()[1] not in months:
            errors += "Invalid date!!!\n"
        if activity.get_date()[0] > 31 or activity.get_date()[2] < 2017 or activity.get_date()[0] <= 0:
            errors += "Invalid date!!!\n"
        if activity.get_date()[1] == "february" and activity.get_date()[0] > 28:
            errors += "Invalid date!!!\n"
        if activity.get_time()[0] < 0 or activity.get_time()[0] > 23 or activity.get_time()[1] > 59 or \
                        activity.get_time()[1] < 0:
            errors += "Invalid Time!!!\n"
        if activity.get_description().isdigit():
            errors += "Please insert a valid description!!!\n"
        if len(errors) > 0:
            raise ValidatorException(errors)

    @staticmethod
    def validate_person(person):
        errors = ""
        if person.get_id() < 0:
            errors += "Invalid Id!!!\n"
        if person.get_name().isdigit():
            errors += "Invalid name!!!\n"
        if person.get_phone() < 0:
            errors += "Invalid phone number!!!\n"
        if person.get_address().isdigit():
            errors += "Invalid address!!!\n"
        if len(errors) > 0:
            raise ValidatorException("Validation errors: "+errors)
