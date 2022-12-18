# write a short command line game

# 1. ask the user for their name: (use the input() function)

# Say hello to them with their name
# If their name begins with a vowel say something funny about that ("Aha! Oho! Uhu! Ihi! etc", your name begins with a vowel!)
# If their n ame begins with a consonant make an even better joke about it.

# Ask them to pick a number between 1 and 10.
# If they guessed the right number, tell them they won
# Else, tell them they lost.

import random
random_number = random.randint(0, 10)
name=input("Enter the name: ")
print(f"Hello.. {name}")
a="aeiouAEIOU"
if(name[0] in a):
    print("Aha! Oho! Uhu! Ihi! etc, your name begins with a vowel!\n")
else:
    print("My dear your name is starting with a constant\n")
number=input("enter a number in between 0 and 10: ")
print(f"Generated random number: {random_number} ")
if(int(number)==random_number):
    print("you won")
else:
    print("you lost")
