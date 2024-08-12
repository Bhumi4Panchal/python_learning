#write the program to accept marks of three subject of students find his percentage and display grade.
marks1 = int(input("Enter marks for subject 1: "))
marks2 = int(input("Enter marks for subject 2: "))
marks3 = int(input("Enter marks for subject 3: "))
total_marks = marks1 + marks2 + marks3
percentage = total_marks / 3
if percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
elif percentage >= 70:
    grade = 'C'
elif percentage >= 60:
    grade = 'D'
elif percentage >= 50:
    grade = 'E'
else:
    grade = 'F'
print("Total Marks:", total_marks)
print("Percentage:", percentage)
print("Grade:", grade)
