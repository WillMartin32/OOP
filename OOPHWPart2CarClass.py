class Car:

    def __init__(self,year,make):
        self.__year_model = year
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        if self.__speed > 0:
            self.__speed -= 5
        else:
            print("Speed can go no lower!")

    def get_speed(self):
        return self.__speed
    