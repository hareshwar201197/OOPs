# Multiple inhiritance  
# multiple parent classes and single child class 

class C:
    def procedure_feature(self):
        print("C is a procedural language ")

class CPP:
    def oops_feature(self):
        print("CPP is object oriented language")

class python(C,CPP):
    def both_feature(self):
        print("python is a Procedural + OOPs features")

python_obj = python()
python_obj.procedure_feature()
python_obj.oops_feature()
python_obj.both_feature()

print(python.mro()) # Method resolution order