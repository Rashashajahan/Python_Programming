# Use string indexing and string concatenation (or f-strings)
# to write the sentence "we see trees" only by picking
# the necessary letters from the given string.

word = "tweezers "
new = word[1]+word[2]+" "+word[-2]+word[2]+word[2]+" "+word[0]+word[-3]+word[2]+word[2]+word[-2]
print(new)
