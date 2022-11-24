# OOP Exercise 8: Determine if School_bus is also an instance of the Vehicle class

class vehicle:
    def __init__(self,name,milage,capaciti):
        self.name=name
        self.milage=milage
        self.capaciti=capaciti

class Bus(vehicle):
    pass
school_bus=Bus("Rani",12,50)
# Python's built-in isinstance() function
print(isinstance(school_bus, vehicle))