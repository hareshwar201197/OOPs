# input from user email id check given input is corect or not
#  hareshwarmali20@gmail.com

import re
email =(input("Enter email From The User : "))
res = re.findall("^[a-zA-Z0-9.]+[@][a-z]+[.][a-z]+$", email)

if res:
    print("your email is correct ")

else:
    print("Your email is Incorrect Try Again ")
