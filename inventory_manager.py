import json
import os

inventory = [
    {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
    {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
    {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25}
]

def display_all():
    print("\nCurrent Inventory")
    print("-" * 48)

    for product in inventory:
        print(f"ID: {product['id']} | Name: {product['name']} | Price: ${product['price']:.2f} | Stock: {product['stock']}")

    print("-" * 48)

def add_product():
    print("\nAdd New Product")

    product_id = input("Product ID: ")

    for product in inventory:
        if product["id"] == product_id:
            print("Product ID already exists!")
            return

    name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))

    new_product = {
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock
    }

    inventory.append(new_product)
    print("Product added successfully!")

def update_stock():
    print("\nUpdate Stock")
    product_id = input("Enter Product ID: ")

    for product in inventory:
        if product["id"] == product_id:
            print("\nProduct Found:")
            print(f"Name: {product['name']}")
            print(f"Current Stock: {product['stock']}")

            new_stock = int(input("New Stock Quantity: "))
            product["stock"] = new_stock

            print("Stock updated successfully!")
            return

    print("Product not found!")

def search_product():
    print("\nSearch Product")
    product_id = input("Enter Product ID: ")

    for product in inventory:
        if product["id"] == product_id:
            print("\nProduct Found")
            print("-" * 48)
            print(f"ID: {product['id']}")
            print(f"Name: {product['name']}")
            print(f"Price: ${product['price']:.2f}")
            print(f"Stock: {product['stock']}")
            print("-" * 48)
            return

    print("Product not found!")

def save_inventory():
    with open("inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)

    print("Inventory saved successfully to inventory.json.")

def load_inventory():
    global inventory

    if os.path.exists("inventory.json"):
        print("inventory.json found.")

        with open("inventory.json", "r") as file:
            inventory = json.load(file)

        print("Inventory loaded successfully!")
    else:
        inventory = []
        print("inventory.json not found. Starting with empty inventory.")

def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)

    load_inventory()

    while True:
        print("\n----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("----------------------------")

        choice = input("\nEnter option: ")

        if choice == "1":
            display_all()
        elif choice == "2":
            add_product()
        elif choice == "3":
            update_stock()
        elif choice == "4":
            search_product()
        elif choice == "5":
            save_inventory()
        elif choice == "6":
            print("\nSaving inventory before exit...")
            save_inventory()
            print("Thank you for using Inventory Management System.")
            break
        else:
            print("Invalid option. Please try again.")


main()


