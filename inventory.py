
from product import Product, PhysicalProduct, DigitalProduct


class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        if self.search_product(product.get_product_id()) is not None:
            print("Product ID already exists.")
            return

        self.__products.append(product)
        print("Product added successfully!")

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product

        return None

    def display_all(self):
        if not self.__products:
            print("Inventory is empty.")
            return

        for product in self.__products:
            product.display_information()

    def get_all_products(self):
        return self.__products.copy()
