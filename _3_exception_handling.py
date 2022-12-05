# str1 = None
# print(len(str1))

class validate_triangle:
    # def __init__(self):
    #     pass

    def valid_triangle(self,base,hight,hypothesis):
        if (base**2 + hight**2 == hypothesis**2):
            print("given valid tringle is ")
        else:
            print("given tringle is not valid")

    def validate_rectangle(self,b,l,B,L):
        if (b==B and l==L):
            print("Valid Rectangle ")
        else:
            print("is not valid rectangle")

tringle_obj = validate_triangle()
tringle_obj.valid_triangle(3,4,5)

tringle_obj.validate_rectangle(2,4,2,4)