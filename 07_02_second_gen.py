# recreate your previous generator that will produce a list of even numbers from 01, 
# but use a generator expression
my_gen = ()  # fill out the code to make it work!
def even(start,stop):
    for i in range(start,stop):
        if i%2==0:
            yield i
my_gen=even(1,20)
# practice using your generator
for i in my_gen:
    print(i)
print("second run!")
# does it work two times?
for i in my_gen:
    print(i)
#Nooooooooooooo. Generator get exhausted.
