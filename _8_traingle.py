# check given tringle is right angle tringle or not 

# input1 = int(input("Enter your first value :"))
# input2 = int(input("Enter your second value :"))
# input3 = int(input("Enter your third value :"))

# if input2 **2 + input3 ** 2 == input1 ** 2:
#     print("Valid tringle")

# elif input1 ** 2 + input2 ** 2 == input3 ** 2:
#     print("Valid tringle")

# elif input3 ** 2 + input1 ** 2 == input2 ** 2:
#     print("valid tringle")
# else:

#     print("Invalid")



# if input1 ** 2 + input2 ** 2 == input3 ** 2 or input2 **2 + input3 ** 3 == input1 ** 2 or input3 ** 2 + input1 ** 2 == input2 ** 2:
#     print("Valid tringle")
# else:
#     print("Invalid")

class traingle_Rectangle:
    def __init__(self,input1,input2,input3):
        self.input1 = int(input("Enter first input :"))
        self.input2 = int(input("Enter second input :"))
        self.input3 = int(input("Enter the third input :"))

    def validate_triangle(self,input1,input2,input3):
        if input2 **2 + input3 ** 2 == input1 ** 2:
            print("Valid tringle")

        elif input1 ** 2 + input2 ** 2 == input3 ** 2:
            print("Valid tringle")

        elif input3 ** 2 + input1 ** 2 == input2 ** 2:
            print("valid tringle")
        else:

            print("Invalid")
    def rectangle(self):
    
     print('enter the values in the order like l,b,l,b ')
     rect1 = input('enter the 1st value of rectangle :  ')
     rect2 = input('enter the 2nd  value of rectangle :  ')
     rect3 = input('enter the 3rd  value of rectangle :  ')
     rect4 = input('enter the 4th value of rectangle :  ')
     if rect1 == rect3 and rect2 == rect4:
       print('valid Rectangle')
     else :
       print(' invalid rectangle')  


traingle_Rectangle_obj = validate_triangle()
