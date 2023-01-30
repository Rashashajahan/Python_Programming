# Write a Python program to flatten a shallow list
#Sample Input: [[2,4,3],[1,5,6], [9], [7,9,0]]
#Output: [2, 4, 3, 1, 5, 6, 9, 7, 9, 0]
def list_flat(list_):
    new=[]
    for element in list_:
        for sub_element in element:
            new.append(sub_element)
    return(new)
print(list_flat([[2,4,3],[1,5,6], [9], [7,9,0]]))
