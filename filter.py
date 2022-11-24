# print only even number

lst = [2,5,23,21,12,22,44,66]

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

def even(lst):
    return lst%2==0

even_lst = list(filter(even,lst))
print(even_lst)

