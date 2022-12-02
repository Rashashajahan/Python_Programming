# Run some basic comparisons on basic integers and floating points

# what is bigger, a or b?
a = 2
b = 10
if (a>b):
    print(f"{a} is greater")
else:
    print(f"{b} is greater")
# What is smaller , c or d?
c = 2.02
d = 2.01119999
if (c<d):
    print(f"{c} is smaller")
else:
    print(f"{d} is smaller")
# what is bigger e or f?
e = float("inf")
f = 12912912912091928312903713582043754302895723048957
if (e>f):
    print(f"{e} is greater")
else:
    print(f"{f} is greater")
# are these equal?

g = 1.02020202020
i = 1.0202020202011111
if (g==i):
    print("They are equal")
else:
    print(f"{g} and {i} are not equal")