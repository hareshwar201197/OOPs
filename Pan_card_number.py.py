import re

pan_number = input("Enter your pan number :")
res = re.findall("^[A-Z]{5}[0-9]{5}[A-Z]{1}$", pan_number)

if res:
    print("Your number is PAN No Is correct ")
else:
    print("Your Pan Numbers is Incorrect")

