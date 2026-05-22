# SMALL BUSINESS INVENTORY & SALES MANAGEMENT SYSTEM
# Programming Fundamentals - Group Coursework

import csv
import os

# GLOBAL DATA STORAGE
inventory = []
sales = []

INVENTORY_FILE = "inventory.csv"
SALES_FILE = "sales.csv"

# CUSTOM EXCEPTIONS
class ProductNotFoundError(Exception):
    """Raised when product ID is not found."""
    pass


class InsufficientStockError(Exception):
    """Raised when stock is insufficient."""
    pass

# SAMPLE DATA
sample_products = [
    ["PRD-0001", "Sugar", "Groceries", 4500, 20],
    ["PRD-0002", "Bread", "Bakery", 3500, 15],
    ["PRD-0003", "Milk", "Dairy", 2800, 10],
    ["PRD-0004", "Rice", "Groceries", 6000, 25],
    ["PRD-0005", "Soap", "Cleaning", 2500, 8],
    ["PRD-0006", "Cooking Oil", "Groceries", 12000, 12],
    ["PRD-0007", "Soda", "Beverages", 2000, 30],
    ["PRD-0008", "Salt", "Groceries", 1500, 5],
    ["PRD-0009", "Tea Leaves", "Beverages", 5500, 7],
    ["PRD-0010", "Biscuits", "Snacks", 3000, 4]
]

# FILE HANDLING FUNCTIONS
def load_inventory():
    """Loads inventory data from CSV file."""

    global inventory

    try:
        if os.path.exists(INVENTORY_FILE):

            with open(INVENTORY_FILE, mode="r", newline="") as file:
                reader = csv.reader(file)
                inventory = []

                for row in reader:
                    inventory.append([
                        row[0],
                        row[1],
                        row[2],
                        float(row[3]),
                        int(row[4])
                    ])

        else:
            inventory.extend(sample_products)

    except Exception as error:
        print(f"Error loading inventory: {error}")



def save_inventory():
    """Saves inventory data to CSV file."""

    try:
        with open(INVENTORY_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(inventory)

    except Exception as error:
        print(f"Error saving inventory: {error}")



def load_sales():
    """Loads sales records from CSV file."""

    global sales

    try:
        if os.path.exists(SALES_FILE):

            with open(SALES_FILE, mode="r", newline="") as file:
                reader = csv.reader(file)
                sales = []

                for row in reader:
                    sales.append([
                        row[0],
                        row[1],
                        row[2],
                        int(row[3]),
                        float(row[4])
                    ])

    except Exception as error:
        print(f"Error loading sales: {error}")



def save_sales():
    """Saves sales data to CSV file."""

    try:
        with open(SALES_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(sales)

    except Exception as error:
        print(f"Error saving sales: {error}")

# UTILITY FUNCTIONS
def generate_product_id():
    """Generates unique product ID."""

    return f"PRD-{len(inventory) + 1:04d}"



def generate_sale_id():
    """Generates unique sale transaction ID."""

    return f"SAL-{len(sales) + 1:04d}"



def find_product(product_id):
    """Finds product by ID."""

    for product in inventory:

        if product[0] == product_id:
            return product

    raise ProductNotFoundError("Product ID not found.")

# PRODUCT FUNCTIONS
def add_product():
    """Registers a new product."""

    try:
        print("\n=== ADD PRODUCT ===")

        product_id = generate_product_id()

        name = input("Enter product name: ").strip().title()
        category = input("Enter category: ").strip().title()

        unit_price = float(input("Enter unit price: "))
        quantity = int(input("Enter quantity in stock: "))

        if unit_price <= 0:
            raise ValueError("Unit price must be greater than zero.")

        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        inventory.append([
            product_id,
            name,
            category,
            unit_price,
            quantity
        ])

        print(f"\nProduct added successfully with ID: {product_id}")

    except ValueError as error:
        print(f"Input Error: {error}")

    except Exception as error:
        print(f"Error: {error}")



def update_stock():
    """Restocks a product."""

    try:
        print("\n=== UPDATE STOCK ===")

        product_id = input("Enter Product ID: ").strip().upper()

        product = find_product(product_id)

        additional_stock = int(input("Enter additional stock quantity: "))

        if additional_stock <= 0:
            raise ValueError("Stock quantity must be greater than zero.")

        product[4] += additional_stock

        print("\nStock updated successfully.")

    except ProductNotFoundError as error:
        print(error)

    except ValueError as error:
        print(f"Input Error: {error}")

    except Exception as error:
        print(f"Error: {error}")



def view_inventory():
    """Displays all products in inventory."""

    try:
        print("\n=== INVENTORY LIST ===")

        print("-" * 95)

        print(
            f"{'ID':<12}"
            f"{'Name':<20}"
            f"{'Category':<18}"
            f"{'Price':<15}"
            f"{'Stock':<10}"
            f"{'Status':<15}"
        )

        print("-" * 95)

        for product in inventory:

            product_id, name, category, price, stock = product

            status = "LOW STOCK" if stock <= 5 else "Available"

            print(
                f"{product_id:<12}"
                f"{name:<20}"
                f"{category:<18}"
                f"{price:<15.2f}"
                f"{stock:<10}"
                f"{status:<15}"
            )

        print("-" * 95)

    except Exception as error:
        print(f"Error: {error}")

# SALES FUNCTIONS
def record_sale():
    """Records product sale transaction."""

    try:
        print("\n=== RECORD SALE ===")

        sale_id = generate_sale_id()

        sale_date = input("Enter sale date (DD/MM/YYYY): ").strip()

        product_id = input("Enter Product ID: ").strip().upper()

        quantity_sold = int(input("Enter quantity sold: "))

        if quantity_sold <= 0:
            raise ValueError("Quantity sold must be greater than zero.")

        product = find_product(product_id)

        if quantity_sold > product[4]:
            raise InsufficientStockError("Insufficient stock available.")

        total_revenue = quantity_sold * product[3]

        product[4] -= quantity_sold

        sales.append([
            sale_id,
            sale_date,
            product_id,
            quantity_sold,
            total_revenue
        ])

        print(f"\nSale recorded successfully. Revenue: {total_revenue:.2f}")

    except ProductNotFoundError as error:
        print(error)

    except InsufficientStockError as error:
        print(error)

    except ValueError as error:
        print(f"Input Error: {error}")

    except Exception as error:
        print(f"Error: {error}")



def sales_report():
    """Displays sales report for a given date."""

    try:
        print("\n=== SALES REPORT ===")

        search_date = input("Enter date (DD/MM/YYYY): ").strip()

        total_units = 0
        total_revenue = 0

        print("-" * 70)

        print(
            f"{'Sale ID':<15}"
            f"{'Product ID':<15}"
            f"{'Quantity':<15}"
            f"{'Revenue':<15}"
        )

        print("-" * 70)

        found = False

        for sale in sales:

            if sale[1] == search_date:

                found = True

                print(
                    f"{sale[0]:<15}"
                    f"{sale[2]:<15}"
                    f"{sale[3]:<15}"
                    f"{sale[4]:<15.2f}"
                )

                total_units += sale[3]
                total_revenue += sale[4]

        print("-" * 70)

        if found:
            print(f"Total Units Sold: {total_units}")
            print(f"Total Revenue: {total_revenue:.2f}")

        else:
            print("No sales found for that date.")

    except Exception as error:
        print(f"Error: {error}")

# LOW STOCK FUNCTION
def low_stock_alert():
    """Displays products with low stock levels."""

    try:
        print("\n=== LOW STOCK ALERT ===")

        found = False

        for product in inventory:

            if product[4] <= 5:

                found = True

                recommended_stock = 20 - product[4]

                print(
                    f"{product[1]} ({product[0]}) -> "
                    f"Current Stock: {product[4]} | "
                    f"Recommended Restock: {recommended_stock}"
                )

        if not found:
            print("No low stock items found.")

    except Exception as error:
        print(f"Error: {error}")

# MENU FUNCTIONS
def display_banner():
    """Displays welcome banner."""

    print("=" * 70)
    print(" CAPITAL CHOICE TRADERS")
    print(" INVENTORY & SALES MANAGEMENT SYSTEM")
    print("=" * 70)



def display_menu():
    """Displays main menu."""

    print("\nMAIN MENU")
    print("1. Add Product")
    print("2. Record Sale")
    print("3. Update Stock")
    print("4. View Inventory")
    print("5. Sales Report")
    print("6. Low Stock Alert")
    print("7. Exit")

# MAIN PROGRAM
def main():
    """Main program execution."""

    load_inventory()
    load_sales()

    display_banner()

    while True:

        display_menu()

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_product()

        elif choice == "2":
            record_sale()

        elif choice == "3":
            update_stock()

        elif choice == "4":
            view_inventory()

        elif choice == "5":
            sales_report()

        elif choice == "6":
            low_stock_alert()

        elif choice == "7":

            save_inventory()
            save_sales()

            print("\nData saved successfully.")
            print("Exiting system...")

            break

        else:
            print("Invalid menu option.")

# PROGRAM ENTRY POINT
if __name__ == "__main__":
    main()
