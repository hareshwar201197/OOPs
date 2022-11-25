# polymorphism
# sigle entity multiple form

# types of polymorphism
# 1. Compile time polymorphism-->not supported in python overloding
# 2. Runtime polymorphism

class compile_time_poly:
    def add(self,no1):
        print(no)
    def add(self,no1,no2):
        print(no1,no2)

obj = compile_time_poly()
obj.add(5,8)