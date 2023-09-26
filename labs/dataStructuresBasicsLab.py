#Author: Daniel Terreros

#Description: A program that puts 100 customers into the queue and assigns a random number of burgers.
import random

def randomName() :
#Fill this list with at least 8 names.
    asCustomers = ["Baby Billy", "Judy", "Keefe", "Kelvin", "Eli", "Jesse", "Benjamin Jason", "Levi"]
    iRandomNum = random.randint(0,len(asCustomers)-1)
    return asCustomers[iRandomNum]

def randomBurgers() :
    return random.randint(1, 20)

strQueue = []

dictCustomer = {}

for iCount in range(100) :
    strQueue.append(randomName)
