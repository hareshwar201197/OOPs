# contex manager

# only one best feature it close file automatically
with open("demo.txt","w") as file:
    file.write("Hey")
    file.close()

is_closed = file.closed
print("is close :",is_closed)



