# write a recursive function to calculate the factorial
"""
    input: 
        n: int
    returns: 
        factorial of n
    
    reminder: factorial 8! is
    8*7*6*5*4*3*2*1
"""
#------------------ without recursion---------------
def factorial(n):
    fact =1
    for i in range (1,n+1):
        fact=fact*i  
    return fact
#-----------------with recursion---------------------
def fact(n):
    if n<=1:
        return 1
    else:
        factt=n*fact(n-1)
    return(factt)
num=int(input("enter the number: "))
print(factorial(num), "is the factorial.")
print(fact(num), "is the factorial.")

