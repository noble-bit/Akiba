# TASK 6 - Employee Payslip

employee_name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))
transport_allowance = float(input("Enter transport allowance: "))
food_allowance = float(input("Enter food allowance: "))

gross_salary = basic_salary + transport_allowance + food_allowance

print("\n========================================")
print("             EMPLOYEE PAYSLIP")
print("========================================")
print("Employee: " + employee_name)
print("Basic Salary:          " + str(basic_salary) + " ETB ")
print("Transport Allowance:    " + str(transport_allowance) + " ETB")
print("Food Allowance:         " + str(food_allowance) + " ETB")
print("----------------------------------------")
print("Gross Salary:          " + str(gross_salary) + " ETB")
print("========================================")
