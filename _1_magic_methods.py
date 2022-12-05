# class Fraction:
#     def __init__(self,n,d):
#         self.num = n
#         self.den = d

#     def __str__(self):
#         return "{}/{}".format(self.num,self.den)

#     def __add__(self,other):
#         temp_num = self.num * other.den + other.num * self.den
#         temp_den = self.den * other.den

#         return "{}/{}".format(temp_num,temp_den)

#     def __sub__(self,other):
#         temp_num = self.num * other.den - other.num * self.den
#         temp_den = self.den * other.den

#         return "{}/{}".format(temp_num,temp_den)

#     def __mul__(self,other):
#         temp_num = self.num * other.num
#         temp_den = self.den * other.den

#         return "{}/{}".format(temp_num,temp_den)

#     def __truediv__(self,other):
#         temp_num = self.num * other.den
#         temp_den = self.den * other.num

#         return "{}/{}".format(temp_num,temp_den)

# x = Fraction(5,7)
# y = Fraction(1,5)

# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)





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