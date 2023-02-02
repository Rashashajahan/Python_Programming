# rewrite your function from the previous exercise (01_01_dry.py)
# this time your function should be able change the divisible by number.
# I should be able to return the list of numbers which is divisible by "n", where
# 'n' can be any number.
## Input: a list of integers, a number 'n'
## output: a new list that only has retains numbers which are divisible by n
lis=[]
a=int(input("enter the number of elements: "))
for s in range(0,a):
    lis.append(int(input()))
number =int(input("enter the number by which the number should be divided: "))
def divis (listt, num):
    res=[]
    for i in listt:
        if (i%num==0):
            res.append(i)
    return res
print(divis(lis,number))