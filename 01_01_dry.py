# convert the following code into a function
# your function should take a single list as input
# it should return a list with only the even numbers from the input list
other_numbers = [213, 2, 3, 125, 12, 32, 21, 3, 6, 23, 12, 3, 326, 45, 12, 32, 14, 2]
numbers = [2, 1, 3, 5, 1, 2, 3, 12, 3, 45, 1, 2, 3]
def eve(listt):
    div_2 = []
    for i in listt:
        if i % 2 == 0:
            div_2.append(i)
    return(div_2)
print(eve(numbers))
print(eve(other_numbers))