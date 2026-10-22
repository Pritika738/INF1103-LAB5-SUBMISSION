
import json
from pathlib import Path

from product import Product
from inventory import Inventory


FILE_PATH = Path(__file__).with_name("inventory.json")


def load_inventory(inventory):
    if not FILE_PATH.exists():
        return

    try:
        with open(FILE_PATH, "r") as file:
            products = json.load(file)

        for item in products:
            product = Product(
                item["product_id"],
                item["name"],
                float(item["price"]),
                int(item["stock"])
            )
            inventory.add_product(product)

        print("Inventory loaded successfully!")

    except (OSError, ValueError, KeyError, TypeError):
        print("Could not load inventory.json.")


def save_inventory(inventory):
    products = []

    for product in inventory.get_all_products():
        products.append(product.to_dict())

    try:
        with open(FILE_PATH, "w") as file:
            json.dump(products, file, indent=4)

        print("Inventory saved successfully!")

    except OSError:
        print("Error saving inventory.")


def main():
    inventory = Inventory()
    load_inventory(inventory)

    while True:
        print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
        print("1. Display all products")
        print("2. Add a product")
        print("3. Update stock")
        print("4. Search for a product")
        print("5. Save inventory")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            inventory.display_all()

        elif choice == "2":
            product_id = input("Enter product ID: ").strip()
            name = input("Enter product name: ").strip()

            try:
                price = float(input("Enter price: "))
                stock = int(input("Enter stock quantity: "))

                if not product_id or not name:
                    print("ID and name cannot be empty.")
                elif price < 0 or stock < 0:
                    print("Price and stock cannot be negative.")
                else:
                    product = Product(
                        product_id, name, price, stock
                    )
                    inventory.add_product(product)

            except ValueError:
                print("Please enter a valid price and stock.")

        elif choice == "3":
            product_id = input("Enter product ID: ").strip()
            product = inventory.search_product(product_id)

            if product is None:
                print("Product not found.")
            else:
                try:
                    quantity = int(input("Enter new stock: "))
                    product.update_stock(quantity)
                except ValueError:
                    print("Please enter a valid whole number.")

        elif choice == "4":
            product_id = input("Enter product ID: ").strip()
            product = inventory.search_product(product_id)

            if product is None:
                print("Product not found.")
            else:
                product.display_information()

        elif choice == "5":
            save_inventory(inventory)

        elif choice == "6":
            save_inventory(inventory)
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    main()
