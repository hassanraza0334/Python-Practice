# Grade Students based on Marks, Grade A B C ,D

marks = int(input("Enter student's Marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
else:
    grade = "D"

print("Grade is:", grade)