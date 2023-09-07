#author: Daniel Terreros

#Description: A program that determines if a number between 1 & 100 is prime.

#Let's deal with 1
print("1 is not a prime number")
for iPrime in range(2, 101) :
    if iPrime == 2 :
        print (iPrime, "is a prime number")
    elif iPrime % 2 == 0 :
        print(iPrime, "is NOT a prime number")