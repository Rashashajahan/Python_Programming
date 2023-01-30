# Write a Python program to convert the nested list to a list of dictionaries
# Sample lists: [["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]]
# Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}
#                   {'color_name': 'Red', 'color_code': '#FF0000'},
#                   {'color_name': 'Maroon', 'color_code': '#800000'},
#                   {'color_name': 'Yellow', 'color_code': '#FFFF00'}]
# use a for-loop
listt=[["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]]
new=[]
a=listt[0]
b=listt[1]
for i in range(0,4):
    new.append(dict(color_name=a[i],color_code=b[i]))
print(new)