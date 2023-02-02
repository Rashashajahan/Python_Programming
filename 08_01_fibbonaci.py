# wrtie a recursive fibonacci function
"""
    input: 
        n: int

    return:
        fibbonacci number for n
    """
#----------------------Without recursion-------------------------------
def fib(num):
    first=0
    sec=1
    a=[0,1]
    for i in range(0,num):
        temp=first
        first=sec
        sec=temp+first
        a.append(sec)
    new=a[num]
    return new
print(fib(10))
print(fib(6))
# fib(6) should return 8
# fib(10) should return 55
#-------------------------with recursion--------------------
def recur_fib(n):
    if n <= 1:
       return n
    else:
       return(recur_fib(n-1) + recur_fib(n-2))
print(recur_fib(10))
print(recur_fib(6))