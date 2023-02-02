# write a function that does not return any variable!
"""
    input: str (a name)
    output: None # no return!
    This function Prints out the users name in all uppercase
    """
def print_your_name_UPPER(name):
    a=name.upper()
#return(a)   here return value is not used, because of that we get NONE as a result
#            if we use return function we get a fully uppercased string
Cap_name=print_your_name_UPPER('rasha')
print(Cap_name)
# What happens when you run your function and attempt to return a variable?
def print_your_name_UPPER(name):
    a=name.upper()
    return a
print(print_your_name_UPPER("lower case name"))
# what is a?   it will be "LOWER CASE NAME"