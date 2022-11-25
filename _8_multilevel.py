# multilevel inheritance

class grandpa():
    def field(self):
        print("field")

class father(grandpa):
    def flat(self):
        print("flat")

    def car(self):
        print("car")

class son(father):
    def bike(self):
        print("bike")

    def mobile(self):
        print("mobile")

son_obj = son()
son_obj.bike()
son_obj.mobile()
son_obj.flat()
son_obj.car()

son_obj.field()

