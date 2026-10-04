# TASK 10 - BMI Health Information

name = input("Enter your name: ")
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

# BMI formula: weight / (height * height)
bmi = weight / (height * height)

print("\n================================")
print("          BMI REPORT")
print("================================")
print("Name: " + name)
print("Weight: " + str(weight) + " kg")
print("Height: " + str(height) + " m")
print("\nBMI: " + str(round(bmi, 2)))
print("================================")
