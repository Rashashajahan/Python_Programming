# Write code that creates a list of all unique values in a list.
# For example:
#list_:[1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
# unique_list = [1, 2, 6, 55, 'hi', 4, 13,]
list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
new=[]
for j in list_:
    if(j not in new):
        new.append(j)
print(new)
