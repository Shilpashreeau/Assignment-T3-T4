#Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
#Make sure to use only higher order functions.

# range is not given in the question. how to do without range??



x=filter(lambda x:x%3!=0 and x%7==0,range(1,100))
print(list(x))