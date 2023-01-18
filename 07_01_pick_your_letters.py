# Use string indexing and string concatenation (or f-strings)
# to write the sentence "we see trees" only by picking
# the necessary letters from the given string.

word = "tweezers "
new = word[1]+word[2]+" "+word[-2]+word[2]+word[2]+" "+word[0]+word[-3]+word[2]+word[2]+word[-2]
print(new)
#######OR##################
a=word[1:3]
b=word[-2:-3:-1]+word[2:4]
c=word[0]+word[-3]+b[::-1]
print(f"{a} { b } {c}")
