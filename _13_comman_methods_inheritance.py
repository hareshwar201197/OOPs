class father:
    def flat(self):
        print("flat")
    def car(self):
        print("Maruti")

class son(father):
    def car(self):
        super().car()   # your target is both are access then use the super keywor to execute imediat parent class method
        print("BMW")

    def mobile(self):
        print("mobile")
son_obj = son()
son_obj.car()