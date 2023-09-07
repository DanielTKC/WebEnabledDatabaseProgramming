#author: Daniel Terreros

#Description: A program that determines if a number between 1 & 100 is prime.

#Let's deal with 1
print("1 is not a prime number")
for iPrime in range(2, 101) :
    if iPrime == 2 :
        print (iPrime, "is a prime number")
    elif iPrime % 2 == 0 : #If it is divisible by 2 and is not 2, then it is not prime.
        print(iPrime, "is NOT a prime number")
    else :
# I've already checked the numbers divisible by 2 so now i need to check odd numbers
        bIsPrime = True #need this to hold the value of true or false so I can use a conditional to print
        for oddCheck in range(3, iPrime, 2): #starts at 3, goes to iPrime -1, in increments of 2(odd)
            if iPrime % oddCheck == 0:
                bIsPrime = False
                break #break out of the loop if it is false
        if bIsPrime :
            print(iPrime, "is a prime number")
        else :
            print(iPrime, "is not a prime number")