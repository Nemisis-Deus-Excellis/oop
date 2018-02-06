class Contact:
    def __init__(self,name,email,subject,message):
        self.__name = name
        self.__email = email
        self.__subject = subject
        self.__message = message

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    def get_email(self):
        return self.__email
    def set_email(self,email):
        self.__email = email

    def get_subject(self):
        return self.__subject
    def set_subject(self,subject):
        self.__subject = subject
#
    def get_message(self):
        return self.__message
    def set_message(self,message):
        self.__message = message
