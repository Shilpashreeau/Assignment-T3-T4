# 1.Write a program which accepts a sequence of comma-separated numbers from console and
#generates a list and a tuple which contains every number in the form of string.
seq=eval(input("enter a sequence\n"))
lst=[]
for i in seq:
    if i==',':
        continue
    else:
        
        lst.append(str(i))
        
print(lst)
print(tuple(lst))

#2.Write a program to reverse a string.
string=input("enter the string\n")
print(string[::-1])


