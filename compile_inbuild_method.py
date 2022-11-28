import re
email = input("Please Enter your Email ID :" )
res = re.compile("^[A-Z][a-zA-Z0-9._]+[@][a-z]+[.][a-z]+$") # only compile and store the result . so you can use your project
result = res.search(email)
print(result)

if res:
    print("Entered Mail is Correct ")

else:
    print("Entered Mail is Incorect")
