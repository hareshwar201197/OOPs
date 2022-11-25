
# Binding Attribute(Variable) and beheviour(Method) together into a single unit 
# Accessing private member thought public enviroment 

class laptop:
    def __init__(self,ram,processor,brand):
        self.ram = ram
        self.processor = processor
        self.brand = brand

        # setter and getter method --> You can specifically modify  variables individually 
    def set_ram(self,ram):
            self.ram = ram

    def get_ram(self):
            return self.ram

    def display(self):
       print("Ram : ",self.ram,"processor :",self.processor, "Brand :",self.brand)
        # return f"/nRam:{self.ram} /nprocessor :{self.processor} /nBrand : {self.brand}"


laptop_obj = laptop("4","i3","DELL")
laptop_obj.display()

print(laptop_obj.set_ram("8"))
(laptop_obj.get_ram())

print(laptop_obj.display())