# Write code that creates a list of all unique values in a list.
# For example:
# list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
# unique_list = [55, 'hi', 4, 13]
# NOTE - you make only keep purely unique values from the original list
# i.e. if it appeared more than once in the first list, you have to remove it entirely.
list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
new=[]
for i in range(0,len(list_)):
    count=0
    for element in list_:
        if(element==list_[i]):
            count+=1
        if(count==0):
            new.append(element)
print(new);;;;;;