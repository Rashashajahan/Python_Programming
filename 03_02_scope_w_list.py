# run the function below
list_of_vowels = ["a", "e", "i", "o", "u"]
def check_for_vowels(string_to_count):
    """
    Function will count if all vowels occur within the string
    """
    for char in string_to_count:
        if char.lower() in list_of_vowels:
            list_of_vowels.remove(char)
    if len(list_of_vowels) == 0:  # all vowels were found, so all vowels removed
        return True
    else:
        return False  # not all vowels found something is still in the list
print(check_for_vowels("aishu"))  # should be false
# run the above function.
print(check_for_vowels("The"))  # this should be False!
print(check_for_vowels("sequoia"))  # should be true
## can you re-use the function?
print(check_for_vowels("abcd")) #it should come false
# what is wrong?
"""output is coming as true"""
## try printing list_of_vowels
print(list_of_vowels)
# why is it empty?
"""After executing the third function call the list of vowels become emplty. As a result for the upcoming execution it will be showing the result as true."""
## Fix the function so this does not happen!
"""To fix the error, we should initialise the list of vowels inside the function"""
def check_for_vowelsss(string_to_count):
    list_of_vowels = ["a", "e", "i", "o", "u"]
    for char in string_to_count:
        if char.lower() in list_of_vowels:
            list_of_vowels.remove(char)
    if len(list_of_vowels) == 0:  # all vowels were found, so all vowels removed
        return True
    else:
        return False
print("-----------------------------------------------------------------------------")
print(check_for_vowelsss("aishu"))  # should be false
print(check_for_vowelsss("The"))  # this should be False!
print(check_for_vowelsss("sequoia"))  # should be true
print(check_for_vowelsss("abcd")) #it should come false