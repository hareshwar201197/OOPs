lst = [4,12,15,45,40,21,31,22]

# def square(data):
#     return data ** 2

# square_lst = list(map(square,lst))
# print(square_lst)

lst = list(map(lambda lst : lst**2,lst))
print(lst)