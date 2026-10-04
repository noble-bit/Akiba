# TASK 8 - Exam Result Report

student_name = input("Enter student name: ")
python_score = float(input("Enter Python score: "))
english_score = float(input("Enter English score: "))
math_score = float(input("Enter Mathematics score: "))

# calculate average
average = (python_score + english_score + math_score) / 3

print("\n========================================")
print("          STUDENT RESULT")
print("========================================")
print("Student: " + student_name)
print("Python:       " + str(python_score))
print("English:      " + str(english_score))
print("Mathematics:  " + str(math_score))
print("----------------------------------------")
print("Average:      " + str(round(average, 2)))
print("========================================")
