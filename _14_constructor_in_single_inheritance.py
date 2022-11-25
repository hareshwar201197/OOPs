class father:
    def __init__(self):
        print("Parent class constructor")

    def flat(Self):
        print("flat")

    def car(self):
        print("car")

class son(father):
    def __init__(self):
        super().__init__()
        print("Child class constructor")

    def bike(self):
        print("bike")

    def mobile(self):
        print("mobile")

son_obj=son()
#son_obj.bike()
#son_obj.mobile()

# parameterize constructor

class college:
    def __init__(self,name,address):
        self.name = name
        self.address = address

class student:
    def __init__(self,student_name,rno,age,name,address):
        super().__init__(name,address)
        self.student_name = student_name
        self.rno = rno
        self.age = age

    def __str__(self):
        return f"Student Name : {self.student_name} \nRno : {self.rno} \nAge :{self.age} \ncollage_Name : {self.college_name} \n collage_address : {self.college_address}"
student_name = input("Enter student name :")
student_name = input("Enter student Rno :")
student_name = input("Enter student Age :")
college_name = input("Enter student college name :")
college_address = input("Enter student college Address :")

student_obj = student(student_name,student_rno,student_age,college_name,college_address)
print(student_obj)

