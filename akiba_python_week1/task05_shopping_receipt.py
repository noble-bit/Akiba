# TASK 5 - Ethiopian Shopping Receipt

customer_name = input("Enter customer name: ")
product_name = input("Enter product name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print("----------------------------------------")
print("              RECEIPT")
print("----------------------------------------")
print("Customer: " + customer_name)
print("Product        Price       Qty")
print("----------------------------------------")
print(product_name + "       " + str(price) + " ETB     " + str(quantity))
print("Total:         " + str(total) + " ETB")
print("Thank you for shopping!")
print("========================================")
