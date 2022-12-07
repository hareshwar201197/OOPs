#printing number from 1 to 24 Skipping multiple of 5

x=1
while x<=24:
    if x%5==0:
        x=x+1
        continue
    print(x)
    x=x+1