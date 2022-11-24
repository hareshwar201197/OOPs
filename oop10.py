#
# Write a program to determine which class a given Bus object belongs to.
# 

class vehicle:
    def __init__(self,name,milage,capacity):
        self.name=name
        self.milage=milage
        self.capacity=capacity

    

class Bus(vehicle):
    pass

# python build in data type
school_bus=Bus("Ratrani",20,50)

print(type(school_bus))

