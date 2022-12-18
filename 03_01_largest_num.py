# Exercise

num_one = 10
num_two = 2
num_three = 1010
num_four = 123

# Use if / else statement to find the largest number.
if(num_one>num_two):
    if(num_one>num_three):
        if(num_one>num_four):
            print(f"{num_one} is greater")
        else:
            print(f"{num_four} is greater")
    else:
        print(f"{num_three} is greater")
else:
    print(f"{num_two} is greater")