# SIMPLE CURRENCY CONVERTER

# Exchange Rates
# 1 USD = 3700 UGX
# 1 EUR = 4000 UGX
# 1 GBP = 4700 UGX

while True:

    print("\n==== CURRENCY CONVERTER ====")
    print("[1] UGX -> USD")
    print("[2] UGX -> EUR")
    print("[3] UGX -> GBP")
    print("[4] Exit")

    choice = input("Select conversion option: ")
    
    if choice == "4":
        print("Exiting currency converter...")
        break

    elif choice not in ['1','2','3']:
        print("Invalid option selected.")
        continue

    try:
        # enter amount in UGX
        ugx_amount = float(input("Enter amount in UGX: "))

        if ugx_amount <= 0:
            print("Amount must be greater than zero.")
            continue

        if choice == "1":
            converted = ugx_amount / 3700
            currency = "USD"

        elif choice == "2":
            converted = ugx_amount / 4000
            currency = "EUR"

        elif choice == "3":
            converted = ugx_amount / 4700
            currency = "GBP"

        #Display converted amount
        print(f"{ugx_amount:.2f} UGX = {converted:.2f}  {currency}")

    except ValueError:
        print("Please enter a valid numeric amount.") 