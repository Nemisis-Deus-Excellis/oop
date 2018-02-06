participantslist=[]
class Participant:
    def __init__(self,username):
       self.__username = username

#USERNAME
    def get_username(self):
        return self.__username
    def append_username(self):
        participantslist.append(self.__username)