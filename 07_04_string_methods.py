# Use a Python string method to prove which of the following files
# are .pdf files, and which aren't.
# Call the method on each file string and print() Python's response.

file_1 = "operators.pdf"
file_2 = "snowfall.jpg"
file_3 = "uncle-joes-wedding.doc"
file_4 = "invitation.pdf"
def check(a):
    if(a[-4:len(a)]==".pdf"):
        return(f"{a} is .pdf file.")
    else:
        return(f"{a} is not a .pdf file.")
print(check("operators.pdf"))
print(check("snowfall.jpg"))
print(check("uncle-joes-wedding.doc"))
print(check("invitation.pdf"))


############OR############
if(file_1.endswith(".pdf")):
    print(f"{file_1} is a pdf file")
else:
    print(f"{file_1} is not a pdf file")
