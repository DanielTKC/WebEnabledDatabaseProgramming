sIndividualOneFullName = input("Enter the full name of individual one: ")
sIndividualOneBirthYear = input("Enter individual one's birth year: ")
iSumOfScores = int(input("How many points total did individual one score on their exams?: "))
iNumberOfTests = int(input("How many tests did they take?: "))

fAverageOfTests = iSumOfScores / iNumberOfTests

print(f"{sIndividualOneFullName} born in {sIndividualOneBirthYear} scored {iSumOfScores} on {iNumberOfTests} for an average of {fAverageOfTests}")

