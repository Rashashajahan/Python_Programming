"""
Modify the function so that x becomes a local variable. There are two ways to do this.
   a. pass x into the function through the arguments
   b. create a new x variable inside the function.
After modifying the function, is the x inside the function the same as the x outside? Are they different? Why or why not?
"""
x = 100
def add_to_me(num):
    x=23
    y = num + x
    print(f"x inside the function is: {x}")
    return y
print(add_to_me(x))
print(f"global variable {x}")  