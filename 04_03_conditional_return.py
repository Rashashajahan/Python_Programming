# write a function that has more than one return statement
"""
    input:
       n: int
       x: int
    returns:
       True if n > x
       False otherwise
    """
def greater_than_x(n, x):
   if(n>x):
      return True
   else:
      return False
print("--------------------Checking n>x ------------------------")
a=int(input("enter the x-value: "))
b=int(input("enter the n-value: "))
print(greater_than_x(b,a))
### Extra credit
# Is it required to use the else block? Can you write the above code with only the if statement but no else?
def greater_than_xx(n, x):
   if(n>x):
      return True
   return False
print("-------------------without else-----------------------------------")
print(greater_than_x(b,a))