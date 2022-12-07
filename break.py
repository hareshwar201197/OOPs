#WAP to build a game give a three chance to use for input a even number
#if use enter a odd numbers in that three chance print "you lost" unless usage
#enter a even no in one chance then rint "You Win"


chance=1


while chance<=3:
    x=int(input("Enter an even number :"))
    if x%2==0:
        break
    chance+=1
    if chance==4:
        print("You Lost")
    else:

        print("You Win")
