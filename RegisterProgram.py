class Registerform:
    def __init__(self, name, gender, email, contact, weight, height, program):
        self.__name = name
        self.__gender = gender
        self.__email = email
        self.__contact = contact
        self.__weight = weight
        self.__height = height
        self.__program = program

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    def get_email(self):
        return self.__email

    def get_contact(self):
        return self.__contact

    def get_weight(self):
        return self.__weight

    def get_height(self):
        return self.__height

    def get_program(self):
        return self.__program



    def set_name(self, name):
        self.__name = name

    def set_gender(self, gender):
        self.__gender = gender

    def set_email(self, email):
        self.__email = email

    def set_contact(self, contact):
        self.__contact = contact

    def set_weight(self, weight):
        self.__weight = weight

    def set_height(self, height):
        self.__height = height

    def set_program(self, program):
        self.__program = program

class Programform:
    def __init__(self, program):
        self.__program = program

    def get_program(self):
        return self.__program