#Exercise

#Write a python program in which read an integer number less than 7 from user

#If the input number is greater than  or equal to 7, then print error message

#If the input is 0 print "Sunday"
#If the input is 1 print "Monday"
#If the input is 2 print "Tuesday"
#If the input is 3 print "Wednesday"
#If the input is 4 print "Thrusday"
#If the input is 5 print "Friday"
#If the input is 6 print "Saturday"

#Use if-else statements
number=int(input("Enter the number: "))
if(number==0):
    print ("Sunday")
elif(number==1):
    print("Monday")
elif(number==2):
    print("Tuesday")
elif(number==3):
    print("Wednesday")
elif(number==4):
    print("Thursday")
elif(number==5):
    print("Friday")
elif(number==6):
    print("Saturday")
else:
    print("Error")