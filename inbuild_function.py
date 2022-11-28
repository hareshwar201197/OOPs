file = open("demo2.txt","w")

# data = file.read() # read the whole data
# print(data)

# data = file.read(5)   # reads only 5 charactors as we mentioned 5 in parameter
# print(data)

# data = file.readline()   # only reads the first line
# print(data)

# data = file.readlines()  # it returns a list of line
# print(data)

# for i in file:  # logicaly read the file
#     print(i,end="")

# file.write("Hello")  # write the data

lst = ["He all\n","Bye All"]
file.writelines(lst)