import  os

# Delete the file
# os.remove("demo1.txt")

# check if file already exist or not
# is_exists = os.path.exists("hari.txt")
# print("is_exists :",is_exists)

# delete Directory (folder)
# it is only deletes the empty folder
# os.rmdir("C:\\Users\\Shree\\Desktop\\Python programs\\.ipynb_checkpoints\\file_handling.py\\Dump")

file = open("D:\\10 CLASS TEST\\harish.txt","w")
file.write("Hi Harish your right")

# x mode 
# Create the file but gives error if the file already exist
file = open("edyoda.txt","x")
file.write("x mode")








