class UserUp:
    def __init__(self,name,username,email,password,region):
        self.__name = name
        self.__username = username
        self.__email = email
        self.__password = password
        self.__region = region

#NA#ME
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
#EMAIL
    def get_email(self):
        return self.__email
    def set_email(self,email):
        self.__email = email

#REGION
    def get_region(self):
        return self.__region
    def set_region(self,region):
        self.__region = region