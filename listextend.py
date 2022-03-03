#Write a program to replace the last element in a list with another list.
lst1=eval(input("enter the list to extend\n"))
lst2=eval(input("enter the list\n"))
lst1.pop()
lst1.extend(lst2)
print(lst1)


#Create a new dictionary by concatenating the following two dictionaries:
#Sample input: a={1:10,2:20} b={3:30,4:40}

a={1:10,2:20}
b={3:30,4:40}
a.update(b)
print(a)
