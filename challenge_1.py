
sub1 = int(input("Enter the mark for Sub 1: "))
sub2 = int(input("Enter the mark for Sub 2: "))
sub3 = int(input("Enter the mark for Sub 3: "))
sub4 = int(input("Enter the mark for Sub 4: "))
sub5 = int(input("Enter the mark for Sub 5: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total / 5)

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"


print("Total Marks:", total, "/ 500")
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
