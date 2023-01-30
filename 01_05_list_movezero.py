# Write a program to move all zero digits to end of a given list of numbers
# Original list:  [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
# Expected output:  [3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

inp = [3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
count=0
out=[]
for i in range (len(inp)):
    if (inp[i]>0):
        out.append(inp[i])
    else:
        count=count+1
while(count>0):
    out.append(0)
    count=count-1
print(out)
        
