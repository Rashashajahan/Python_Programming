## Write a generator that will produce a list of even numbers
# use a function
"""
    input:
        start: int
        stop: int
    returns:
        generator object

    Your function should create a generator object that will
    be the sequence of even numbers from start to stop
    Make sure to use the yield keyword!
"""
def list_of_even_nums(start, stop):
    while start<stop:
        if (start%2==0):
            yield start
        start = start+1
# use your generator
for i in list_of_even_nums(2, 11):
    print(i)
## should print out 2,4,6,8,10
#-----------------OR__________________
def even_num(start,stop):
    for i in range(start,stop):
        if i%2==0:
            yield i
for ele in even_num(2,23):
    print(ele)
