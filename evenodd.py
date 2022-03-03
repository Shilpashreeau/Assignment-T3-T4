#Write a function called showNumbers that takes a parameter called limit. It should print all the
#numbers between 0 and limit with a label to identify the even and odd numbers.
def showNumbers(a,lmt):
    for i in range(a,lmt+1):
        if i%2==0:
            print("\nEVEN", i)
        else:
            print("\n ODD", i)

showNumbers(0,4)