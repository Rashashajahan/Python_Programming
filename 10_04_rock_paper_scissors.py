# write rock-paper-scissors game

# have the user play against the computer
# you can use the random library to select an option for the computer

# use a while loop so the user can play until they win
import random

computer_choice = random.randint(1, 3)

# you can map each of rock / paper / scissors to an integer from 1 - 3
import random
computer_choice = random.randint(1, 3)
print("rock = 1 \npaper = 2 \nscissors = 3 \n")
status=0
while(status==0):
    i=input("enter the choice: ")
    i=int(i)
    if(i):
        print(computer_choice)
        if(computer_choice==1): 
            if(i==1):
                print("invalid")
                continue
            elif(i==3):
                print("computer won")
                continue
            else:
                print("You won!")
                status=1
        elif(computer_choice==2):
            if(i==2):
                print("invalid")
                continue
            elif(i==1):
                print("computer won")
                continue
            else:
                print("You won!")
                status=1
        else:
            if(i==3):
                print("invalid")
                continue
            elif(i==2):
                print("computer won")
                continue
            else:
                print("You won!")