#Create a new list which contains the specified numbers after removing the even numbers from a
#predefined list.
lst=[1,2,3,4,5,6]
for i in lst:
    if i%2==0:
        lst.remove(i)
print(lst)