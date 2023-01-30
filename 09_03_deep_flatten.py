# Make your list flatten code do a DEEP flatten and account for other datatypes
hard_nested_list = [
    [1, 2, [1, [1, 2], 2], 3, 4],
    [5, 6],
    [7, 8, 9],
    "shiva",
    10,
    [1, 2, [8, 9,], "Devi"],
    10.0,
    (1, 2),
]
# should get back
# [1, 2, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 'brandon', 10, 10.0, 1, 2]
many_nests = ["a", ["bb", ["ccc", "ddd"], "ee", "ff"], "g", "h"]
# should get back
# ['a', 'bb', 'ccc', 'ddd', 'ee', 'ff', 'g', 'h']

final_list = []
while (True):
    for element in many_nests:
        if isinstance(element, (list,tuple)):
            final_list.extend(element)
        elif isinstance(element, (int,float,str)):
            final_list.append(element)
    for element in final_list:
        if isinstance(element, (list,tuple)):
            many_nests=final_list
            final_list=[]
            break
    else:
        break
print("Before")
print(many_nests)
print("-------------------------------------------------------------------------------------------")
print(final_list)