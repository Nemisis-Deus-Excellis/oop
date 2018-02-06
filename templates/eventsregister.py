class Participant:
    def __init__(self,first_name,last_name,phone,email,):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__phone = phone
        self.__email = email
#NAME
    def get_first_name(self):
        return self.__first_name
    def set_first_name(self,first_name):
        self.__first_name = first_name

    def get_last_name(self):
        return self.__last_name
    def set_last_name(self,last_name):
        self.__last_name = last_name
#USERNAME
    def get_phone(self):
        return self.__phone
    def set_username(self,phone):
        self.__phone = phone

#EMAIL
    def get_email(self):
        return self.__email
    def set_email(self,email):
        self.__email = email


