# input--> 1800 0002 2020
# output--> 18 2 22

import re
data = "1800 0002 2020 220000"
sub_meth = re.sub(r'0','',data)  # Remove Any Value
print(sub_meth)

