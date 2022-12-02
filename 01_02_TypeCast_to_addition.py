#Type casting Exercise - 2
# Addition of string and integer using explicit conversion
# Initialise a string variable and integer variable
a = 10
b = "10"
# After explicit conversion, use python to successfully perform
# the addition of these variables - print the result to the console
b=int(b)
c=a+b
print(f"{a} + {b} = {c}")
## Now try to convert this variable
c = "ten"
d=int(c)
print(type(d))

e=float(c)
print(type(e))
## What kind of error does python give?
        #anser:invalid literal
## What do you think the reason is?