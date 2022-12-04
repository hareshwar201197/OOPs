# 8-16--->{8-16}
# Atleast one upper latter
# Atleast one upper latter
# Atleast one digit
# Special charactor
import re

password = input("Enter Your Password :")
res = re.findall(r"^.*(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=])){8,16}.*$",password)
print(res)

if res:
    print("Correct Format :")
else:
    print("Incorrect Formate :")

    