#Write a Python program to create a Vehicle
#class with max_speed and mileage instance attributes.

class vehical:
    def __init__(self,max_speed,milage):
        self.max_speed=max_speed
        self.milage=milage

model=vehical(10,120)
print(model.max_speed,model.milage)

"""a=model.max_speed,model.milage
print(a)"""
