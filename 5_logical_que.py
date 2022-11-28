# Que 1] Given numbers = range(20), produce a list containing the word 'even'
# odd number print even word & even number print Odd word
# result = ["even" if n%2 == 0 else "odd" for n in range(20)]
# print(result)

# lst = [1,2,3,4,5]
# res = [i if i%2==0 else "" for i in lst]
# print(res)
# else hai to age likhna hai nahi hai to end me likhna hai

# Que 2] Given String Start with B check

# str1 = "Bharti"

# data = lambda x : "Is Start with B " if x.startswith('B') else "Is Not Strat with B"
# print(data(str1))

# Que 3] Given input lst =[5,6,7,4,2,2]
# O/P --> ["odd","even","odd","even","even","even"]
# lst = [5,6,7,4,2,2]
# for i in lst:
#     if i%2==0:
#         print("even")
#     else:
#         print("odd")

# odd_even = lambda lst : 'even' if lst % 2 == 0 else 'odd'
# data = list(map(odd_even,lst))
# print(data)

# lst = [12,15,17,30,33,25]
# o/p--> new_lst = [15,30] Should be divisible by 3 & 5
"""new_lst=[]
for  i in lst:
    if i % 3==0:
        new_lst=lst.append(i)
        print(new_lst)
    if i % 5==0:
        new_lst=lst.append(i)
        print(new_lst)"""

# num = int(input("Enter the Number :"))
# str1 = str(num)
# dict = {'0':'Zero','1':'One','2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine'}
# data = [dict[i] for i in str1]
# for j in data:
#     print(j,end=" ")
# print()

str1 = input("Enter first string :")
str2 = input("Enter Second string :")

lst1 = str1.split(" ")
lst2 = str2.split(" ")
data = [[i for i in lst1 if i not in lst2],[j for j in lst2 if j not in lst1]]
for s in data:
    for s1 in s:
        print(s1,end=" ")
print()