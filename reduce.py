from functools import reduce

# sum of all numbers 
lst = [12,11,21,33,21,23,99]
"""
def sum(data):
    sums = 0
    for i in data:
        sums +=i

    return sums

result = sum(lst)
print(result)
"""

def sum(data1,data2):
    return data1 + data2

result = reduce(sum,lst)

print(result)
