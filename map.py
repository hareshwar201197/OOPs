# print square of the list
"""lst = [4,12,15,45,40,21,31,22]
def square(data):
    sq_lst = []
    for i in data:
        sq = i**2
        sq_lst.append(sq)
    return sq_lst

square_lst = square(lst)
print(square_lst)

"""
lst = [4,12,15,45,40,21,31,22]

def square(data):
    return data ** 2

square_lst = list(map(square,lst))
print(square_lst)
