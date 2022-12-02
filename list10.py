"""# How to Find a perticular index value of element
sum=0
for i in [11, 21, 51, 101, 111, 151, 201]:
    sum=sum+i
print(sum)
"""

"""a=(1,2,3)
b=(1,2,3)
print(id(a[0])==id(b[0]))"""

n=int(input("Enter the number: "))
i=1
sum=0
while i <= n:
    sum=sum+i
    i=i+1
print(sum)
