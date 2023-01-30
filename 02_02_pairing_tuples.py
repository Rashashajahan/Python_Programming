### This code creates a random list for you to use
# Write a script that takes 'new' (a list of numbers) and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.
#You will need a python function called `sort`
# example input :[1,2,5,1,2]
# example output :[(1,1), (2,2), (5,0)]
import random
list_length = random.randint(1, 20)
new=[]
for i in range(list_length):
    new.append(random.randint(1, 100))
new.sort()
if((len(new)%2)!=0):
    new.append(0)
res=[]
for j in range(0,len(new),2):
    res.append(tuple([new[j],new[j+1]]))  
print(res)