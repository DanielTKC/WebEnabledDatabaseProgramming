#Description: Final Grade calculator

#author: Daniel Terreros

sName = input("What is the name of the student? ").upper()
iFinalGradeAverage = int(input("What was their final grade average? "))

if (iFinalGradeAverage >= 94) and (iFinalGradeAverage <= 100) :
    sLetterGrade = "A"
else : sLetterGrade = "F"

print(sName, "had a final grade average of", iFinalGradeAverage, "which resulted in a(n)", sLetterGrade, "for the course.")

