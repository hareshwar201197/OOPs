import re

Adhar = (input("Enter your Adhar Number :"))
res = re.findall("^[1-9]{1}[0-9]{3}[-][0-9]{4}[-][0-9]{4}$",Adhar)

if res:
    print("Your Adhar Number Is Correct Than You ")
else:
    print("Your Adhar Number is Not Valid . Check Yor Adhar Number")


