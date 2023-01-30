# stage 1
# Write a program to count the number of strings where the string length is 2 or more
# sample list: ['aaaa', 'a', 'ab', 'abc', ]
# result : 3
input=['aaaa', 'a', 'ab', 'abc', ]
count=0
for i in input:
    if(len(i)>1):
        count+=1
print(count)
## Stage 2
# Now count the number of strings that have length 2 or more
# AND the first and last character are same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
input2=['abc', 'xyz', 'aba', '1221']
count1=0
for i in input2:
    length=len(i)
    if(length>1 and i[0]==i[-1]):
        count1+=1
print(count1)