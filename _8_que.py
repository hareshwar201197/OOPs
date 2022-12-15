# 1  2  3  4  5  
# 1  2  3  4  5
# 1  2  3  4  5
# 1  2  3  4  5
# 1  2  3  4  5
n = int(input("Enter the number of rows : "))
for i in range(n):
    for j in range(n):
        print(str(j+1),end='  ')
    print()

