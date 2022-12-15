# s = 'Python,Java,C,C++'
# print(s[10:1:-2])


import re
sentence = "we are human"
matched = re.matched(r'(.*) (.*?) (.*)',sentence)
print(matched.groups())

