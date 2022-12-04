import re
Pin =(input("Enter Pincode From The User : "))
res = re.findall("^[1-9]{1}[0-9]{5}$", Pin)

if res:
    print("Formate is Fine")

else:
    print("Formate is Incorrect")
