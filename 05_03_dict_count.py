# Write a program to create a dictionary from a string.
# Track the count of the letters from the string.
# Sample string : 'securecoding'
# Expected output: {'s': 1, 'e': 2, 'c': 2, 'u': 1, 'r': 1, 'o': 1, 'd': 1, 'i': 1, 'n': 1, 'g': 1}
inp=input("enter the string: ")
a=tuple(inp)
dictt={}
for i in range(0,len(inp)):
    count=0
    for ele in a:
        if(a[i]==ele):
            count=count+1
        dictt.update({a[i]:count})
print(dictt)
    

