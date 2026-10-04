# TASK 9 - Currency Exchange Desk

# fixed exchange rate
exchange_rate = 150

usd_amount = float(input("Enter USD Amount: "))

# convert to ETB
etb_amount = usd_amount * exchange_rate

print("\n==============================")
print("      CURRENCY EXCHANGE")
print("==============================")
print("USD Amount: " + str(usd_amount))
print("Exchange Rate: 1 USD = " + str(exchange_rate) + " ETB")
print("ETB Amount: " + str(etb_amount) + " ETB")
print("==============================")
