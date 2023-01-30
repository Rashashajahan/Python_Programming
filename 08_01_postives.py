# Use a list comprehension to create a list called `positive` from the list
# `numbers` that contains only the positive numbers from the provided list.

numbers = [5, -8, 3, 10, -19, -22, 44, 2, -1, 4, 42]
positive=[i if i>0 else "" for i in numbers]
print(positive)
