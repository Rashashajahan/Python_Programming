# create a list that contains a tuple for each word.
# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]
inp=input("enter the input : ")
splitt=inp.split()
result=[]
for i in splitt:
    result.append(tuple(i))
print(result)