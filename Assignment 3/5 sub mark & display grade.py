total = 0
for i in range(5):
    marks = float(input("Enter marks of Subject " + str(i+1) + ": "))
    total += marks

average = total / 5

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print("Total Marks:", total)
print("Average Marks:", average)
print("Grade:", grade)