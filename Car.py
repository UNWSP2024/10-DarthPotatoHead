#Program Written By: Ainsley Bellamy
#Date Written: 04/03/2025
#Program Title: Car_Simulation


# Program # 2: Car Class
# Write a class named Car that has the following data attributes:

# __year_model (for the car's year model)
# __make (for the make of the car)
# __speed (for the car's current speed)
# The Car class should have an __init__ method that accepts the car's year model and make as arguments.  These values should be assigned to the object's __year_model and __make data attributes.  It should also assign 0 to the __speed data attribute.

# The class should also have the following methods:

# The accelerate method should add 5 to the speed data attribute each time it it called.
# The brake method should subtract 5 from the speed data attribute each time it is called.
# The get_speed method should return the current speed.
# Next, design a program that creates a Car object then calls the accelerate method five times.  After each call to the accelerate method, get the current speed of the car and display it.  The call the brake method.  After each call to the brake method, get the current speed of the car and display it.

import time
#Define a class that defines year and model, make, and methods that can be applied to each attribute.
class Cars:
    def __init__(self, yearModel, make):
        self.__year_model = yearModel
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed = self.__speed + 5

    def get_speed(self):
        return self.__speed

    def brake(self):
        self.__speed = self.__speed - 5

    def get_yearModel(self):
        return self.__year_model

    def get_make(self):
        return self.__make

#Function to simulate acceleration of the car object passed as an argument.
def acceleration(car):
#First print which car is accelerating.
    print(f"Year & Model: {car.get_yearModel()}\nMake: {car.get_make()}")
    print("-------------------------------")
    print(f"Accelerating ", end="")
#Using time.sleep() makes it more entertaining.
    for i in range(3):
        time.sleep(1)
        print(". ",end="")
    print()
#Calling the accelerate method 5 times will change the self.__speed attribute to 25, adding 5 each time.
    for i in range(5):
        time.sleep(1)
        car.accelerate()
        print(car.get_speed(), "mph")

#Simulate braking fast.
def deceleration(car):
    for i in range(5):
        time.sleep(0.5)
        car.brake()
        print(car.get_speed(), "mph")

#Define objects and call above functions.
def main():
    car1 = Cars("2015, Pilot", "Honda")
    car2 = Cars("2020, Cybertruck", "Tesla")
    acceleration(car1)
    deceleration(car1)
    print("------------------------------")
    acceleration(car2)
    deceleration(car2)

if __name__ == '__main__':
    main()


