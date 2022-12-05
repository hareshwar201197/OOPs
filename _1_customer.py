class customer:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def intro(self):
        print("i am",self.name,"and my age",self.age)

c1 = customer("harish",21)
c2 = customer("Saurabh",22)
c3 = customer("kundan",23)
c4 = customer("ganesh",24)

L = [c1,c2,c3]
for i in L:
    i.intro()

    