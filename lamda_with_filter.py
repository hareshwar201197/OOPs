# print only even number

# lst = [2,5,23,21,12,22,44,66]

# Normal Way
"""def even(lst):
    even_lst = []
    for i in lst:
        if i%2==0:
            even_lst.append(i)
    return even_lst

elst = even(lst)
print(elst)
"""
# Same que solve using filter
# Ussing filter
# def even(lst):
#     return lst%2==0

# even_lst = list(filter(even,lst))
# print(even_lst)

# Ussing filter with lambda

lst = (2,5,23,21,12,22,44,66)

even_lst = list(filter(lambda lst : lst%2==0,lst))
print(even_lst)


even_lst = tuple(filter(lambda lst : lst%2==0,lst))
print(even_lst)