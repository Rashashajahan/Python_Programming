# You start this journey with a number `n`.
# You have to display a string representation of all numbers from 1 to n,
# but there are some constraints:
# - If the number is divisible by 3, write `Fizz` instead of the number
# - If the number is divisible by 5, write `Buzz` instead of the number
# - If the number is divisible by both 3 and 5, write `FizzBuzz` instead of the number

# feel free to adjust n for debugging
n = 0
while(n <= 100 ):
    if(n%3 == 0):
        if(n%5 == 0):
            print(f"{n} is FizzBuzz")
        else:
            print(f"{n} is Fizz")
        n=n+1
    elif(n%5 == 0):
        print(f"{n} is Buzz")
        n=n+1
    else:
        n=n+1
