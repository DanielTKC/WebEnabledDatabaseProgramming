#Description: Final Grade calculator

#author: Daniel Terreros

sName = input("What is the name of the student? ").upper()
iFinalGradeAverage = int(input("What was their final grade average? "))

if (iFinalGradeAverage >= 94) and (iFinalGradeAverage <= 100) :
    sLetterGrade = "A"
elif (iFinalGradeAverage >= 90) and (iFinalGradeAverage <= 93) :
    sLetterGrade = "A-"
elif (iFinalGradeAverage >= 87) and (iFinalGradeAverage <= 89) :
    sLetterGrade = "B+"
elif (iFinalGradeAverage >= 83) and (iFinalGradeAverage <= 86) :
    sLetterGrade = "B"
elif (iFinalGradeAverage >= 80) and (iFinalGradeAverage <= 82) :
    sLetterGrade = "B-"
elif (iFinalGradeAverage >= 77) and (iFinalGradeAverage <= 79) :
    sLetterGrade = "C+"
elif (iFinalGradeAverage >= 73) and (iFinalGradeAverage <= 76) :
    sLetterGrade = "C"
elif (iFinalGradeAverage >= 70) and (iFinalGradeAverage <= 72) :
    sLetterGrade = "C-"
elif (iFinalGradeAverage >= 67) and (iFinalGradeAverage <= 69) :
    sLetterGrade = "D+"
elif (iFinalGradeAverage >= 63) and (iFinalGradeAverage <= 66) :
    sLetterGrade = "D"
elif (iFinalGradeAverage >= 60) and (iFinalGradeAverage <= 62) :
    sLetterGrade = "D-"
elif (iFinalGradeAverage <=59) :
    sLetterGrade = "F"
else : sLetterGrade = "Error"

print(sName, "had a final grade average of", iFinalGradeAverage, "which resulted in a(n)", sLetterGrade, "for the course.")

