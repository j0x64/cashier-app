# Cashier program made in Python

# Importing necessary libraries
import os; from os import system as command

# Create a function related to cashier-needs
def add_items():
    """Add items to the itemlist"""
    items = []
    while True:
        item_name = input('Enter the item name (or type "done" to finish): ')
        if item_name.lower() == 'done':
            break
        try:
            item_price = float(input(f'Enter the price for {item_name}: $'))
            items.append({"name": item_name, "price": item_price})
        except ValueError:
            print('Invalid price! Please enter a number.')
    return items

def calculate_total(items):
    """Calculate total items price"""
    total = sum(item['price'] for item in items)
    return total

def process_payment(total):
    """Process the payment of a selected items"""
    while True:
        try:
            payment = float(input(f"The total is ${total:.2f}. Enter payment amount: $"))
            if payment < total:
                print(f"Insufficient payment. You still owe ${total - payment:.2f}.")
            else:
                change = payment - total
                return change
        except ValueError:
            print("Invalid amount! Please enter a number.")

def print_receipt(items, total, change):
    """Print and display the total receipt of an item"""
    print("\n--- Receipt ---")
    for item in items:
        print(f"{item['name']}: ${item['price']:.2f}")
    print(f"Total: ${total:.2f}")
    print(f"Change: ${change:.2f}")
    print("Thank you for shopping with us!")
    print("---------------\n")

# Handle all the functions at one set
def main():
    print("Welcome to the Cashier Program!")
    items = add_items()
    if items:
        total = calculate_total(items)
        change = process_payment(total)
        print_receipt(items, total, change)
    else:
        print("No items entered. Exiting.")

# Run the program
if __name__ == "__main__":
    main()