# GREENFIELD TRADING COMPANY RECEIPT GENERATOR

company_name = "GREENFIELD TRADING COMPANY"

customer_name = input("Hello! what's your name: ")
date = input("What's the date today (DD/MM/YYYY): ")

item1 = input("Enter your first item: ")
price_item1 = float(input("Enter the first item price: "))

item2 = input("Enter your second item: ")
price_item2 = float(input("Enter the second item price: "))

item3 = input("Enter your third item: ")
price_item3 = float(input("Enter the third item item price: "))

subtotal = price_item1 + price_item2 + price_item3
vat = subtotal * 0.16
total = subtotal + vat

print("\n-----------------------------------------------")
print(company_name)
print(f"Customer: {customer_name}          Date: {date}")
print("-------------------------------------------------")

print(f"{item1:<20}        {price_item1:.2f}")
print(f"{item2:<20}        {price_item2:.2f}")
print(f"{item3:<20}        {price_item3:.2f}")

print("-------------------------------------------------")
print(f"Subtotal:                    {subtotal:.2f}")
print(f"VAT (16%):                   {vat:.2f}")
print(f"TOTAL:                       {total:.2f}")
print("-------------------------------------------------")