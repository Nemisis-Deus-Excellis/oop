class Bmi:
    def __init__(self, height, weight):
        self.__height = height
        self.__weight = weight

    def get_height(self):
        return self.__height

    def get_weight(self):
        return self.__weight

    def set_height(self, height):
        self.__height = height

    def set_weight(self, weight):
        self.__weight = weight

    def get_bmi(self):
        return self.__weight / self.__height ** 2