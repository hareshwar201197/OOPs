class array:
    def __init__(self,fix_size):
        self.fix_size=fix_size
        self.lenght=0
        self.data=[]
    
    def add(self,element):
        if self.lenght<self.fix_size:
            self.data.append(element)
            self.lenght +=1
        else:
            print("Array is full")

    def remove(self,index):
        for i in range(self.lenght):
            if i==index:
                del self.data[index]
                self.lenght-=1
            else:
                print("No such Index Found")

    def insert(self,index,element):
        if self.lenght<self.fix_size:
            for i in range(self.lenght):
                if i==index:
                   self.data[i]=element
                   self.lenght+=1

obj=array(4)
obj.add(10)
obj.add(20)
obj.add(30)
obj.remove(50)
print(obj.data)

