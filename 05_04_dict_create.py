# Write a script that creates a dictionary of keys, `n`
# and values `n * n` for numbers 1 to 10. For example:
# result = {1: 1, 2: 4, 3: 9, ... and so on}
# use a for-loop
dict={n:n*n for n in range (1,10)}
print(dict)

###########OR##############

dictt={}
for i in range(1,10):
   dictt.update({i:i*i})
print(dictt) 