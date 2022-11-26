row = int(input("Enter Rows :"))
cols = int(input("Enter Cols :"))

matrix=[]
for i in  range(row):
    rows=[]
    for j in range(cols):
        element=int(input("Enter Element : "))
        rows.append(element)
    matrix.append(rows)

print(matrix)