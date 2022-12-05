# Block
# try --> it is store suspious code
# except --> is use to handle the exception

class exp_handling:
    def divide(self):
        div = 0
        no1 = int(input("Enter no1 : "))
        no2 = int(input("Enter no2 : "))

        try:
            div = no1 / no2
        except:
            print("Exception Handle")
        print("Division :",div)
        print("End of program ")

obj = exp_handling()
obj.divide()
