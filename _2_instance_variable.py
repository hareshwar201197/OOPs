# instance variable
# define inside the method / constructor with "self." as prefix
# scope throught the class 


class student:
    def info(self):
        self.name = "Hareshwar"
        self.rno = 20

    def display(self):
        print("Name :" ,self.name)
        print("Rno :",self.rno)

student_obj = student()
student_obj.info()
student_obj.display()
