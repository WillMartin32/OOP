import OOPHWPart2CarClass as cc

model_year = "2016"
car_make = "Jeep"

a = 0
b = 0

car = cc.Car(model_year,car_make)

while a < 5:
    car.accelerate()
    a += 1
    print("--The current speed of the car is", car.get_speed())


while b < 5:
    car.brake()
    b += 1
    print("--The current speed of the car is", car.get_speed())

