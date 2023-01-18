# Find the index of the first occurrence of the letter `n` in the string.

composer = "Ludvig van Beethoven"
for i in range(0, len(composer)):
    if(composer[i]=="n"):
        print(i)
        break
print(composer.find("n"))
#if the letter is not found then we get -1.
