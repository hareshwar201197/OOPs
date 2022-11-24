# setter and Getter methods
class Student:
    def setName(self,name):
        self.name=name
    def getName(self):
        return(self.name)
    def setMarks(self,marks):
        self.marks=marks
    def getMarks(self):
        return self.marks

n=int(input("Enter The Number of Student :"))
student=[]

for i in range(n):
    s=Student()
    name=input("Enter The student name :")
    marks=int(input("Enter the student Marks :"))
    s.setName(name)
    s.setMarks(marks)
    student.append(s)

for s in student:
    print('Hi',s.getName())
    print('Your marks are :',s.getMarks())