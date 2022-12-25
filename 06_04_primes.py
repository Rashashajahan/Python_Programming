# Write a python program to print all prime numbers between 0 to 100 , and print how many prime numbers are there
def prime_numbers(num):
    listt=[]
    if(num>1):
        for i in range(2,num+1):
            count=0
            for j in range(1,i+1):
                if(i%j==0):
                    count+=1
            if (count==2):
                listt.append(i)
        return listt, (f"Number of prime number is {len(listt)}")
print(prime_numbers(100)) 
