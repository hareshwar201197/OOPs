

class special_method:

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def __add__(self,self1):
        return self.salary + self1.salary

    def __mul__(self,self1):
        return self.salary * self1.salary

    def __len__(self):
        return len(self.name)

obj = special_method("Ram",1000)
obj1 = special_method("Krushna",2000)

print(obj + obj1)
print(obj * obj1)

print(len(obj))