from functools import reduce

# sum of all numbers 
data = [12,11,21,33,21,23,99]

# def sum(data1,data2):
#     return data1 + data2

# result = reduce(sum,lst)

# print(result)

lst = reduce(lambda data1,data2 : data1 + data2, data)
print(lst)