# Exercise

# Write a program to find the largest number in a list without using built-in functions

# [1,2,1,3,123123,2,1,3,6,3,1,23,6,123,1235,]
# output = 123123

# use a for loop
a=[1,2,1,3,123123,2,1,3,6,3,1,23,6,123,1235,]
larger=a[0]
for element in a:
    if(larger<element):
        larger=element
print(larger)
