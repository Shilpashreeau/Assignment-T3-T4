#Write a function to compute 5/0 and use try/except to catch the exceptions
from decimal import DivisionByZero

def Div(n):
    try:
        n/0
    except:
        print("cannot divide 5 by 0")
#finally:
   # print("execute anyways")
Div(5)