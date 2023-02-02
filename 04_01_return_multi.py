# Write a function that returns multiple values
# example idea:
"""
    Input:
        first_name: str
        last_name: str
    returns:
        first_name, last_name 

    This function takes the first name and last name and lowercases them

    example input: GILAD GRESSEL
    output: gilad gressel
    """
def lower_names(first_name, last_name):
    lf=first_name.lower()
    ll=last_name.lower()
    return lf, ll
f_name=input("enter your first name: ")
l_name=input("enter the last name: ")
print(lower_names(f_name,l_name))
names = lower_names("GILAD", "GRESSEL")  # what datatype is names?
print(names)
print(type(names))

