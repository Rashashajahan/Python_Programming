# Write a script that takes the following two dictionaries 
# and creates a new dictionary by combining the common keys
# and adding the values of duplicate keys together.
# Use `for` loops to iterate over these dictionaries
# to accomplish this task.
# Example output:
# result = {"a": 3, "b": 2, "c": 7 , "d": 2}

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4, "d": 2}
for key1 in dict_1:
    for key2 in dict_2:
        count=0
        if(key1==key2):
            count=dict_1[key1]+dict_2[key2]
            dict_2.update({key1:count})
    val=dict_1[key1]
    if(key1 not in dict_2):
        dict_2.update({key1:val})
print(dict_2)
