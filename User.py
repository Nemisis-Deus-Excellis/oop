class User:
    def __init__(self,name,username,age,email,password):
        self.__name = name
        self.__username = username
        self.__age = age
        self.__email = email
        self.__password = password

#NAME
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
#USERNAME
    def get_username(self):
        return self.__username
    def set_username(self,username):
        self.__username = username

#PASSWORD
    def get_password(self):
        return self.__password
    def set_password(self,password):
        self.__password = password
#AGE
    def get_age(self):
        return self.__age
    def set_birthdate(self,age):
        self.__age = age
#EMAIL
    def get_email(self):
        return self.__email
    def set_email(self,email):
        self.__email = email


