#Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1
#and n(both 1 and n included).
dict={}
n=int(input("enter the number of items to be inserted into dict\n"))

x=1

while x<=n:
    
    dict[x]=x*x
    dict.update()
    x+=1

print(dict)