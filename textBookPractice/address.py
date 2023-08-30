#Author: Daniel Terreros
#Description: A program that asks information then formats it.

#Gather information

import datetime

sFirstName = input("Enter your first name? ").upper()
sLastName =  input("Enter your last name? ").upper()
sStreetAddress = input("What is your street address? ")
sCity = input("What is your city? ")
sState = input("What is your state? ")
sBirthYear = input("What year were you born? ")
today = datetime.date.today()
iYear = today.year
iBirthYear = int(sBirthYear)
iYearsOld = iYear - iBirthYear

#Print the information

print(sFirstName, sLastName)
print(sStreetAddress)
print(sCity,sState, sep="\t")
print("In " + str(iYear) + " " + sFirstName + " is " + str(iYearsOld)  + " years old.")

