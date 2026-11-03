from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def update_stock(self, quantity):
        if quantity < 0:
            print("Stock cannot be negative.")
            return False

        self.__stock = quantity
        print("Stock updated successfully!")
        return True

    def display_information(self):
        print(f"ID: {self.__product_id}")
        print(f"Name: {self.__name}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock: {self.__stock}")
        print("--------------------")

    def to_dict(self):
        return {
            "product_id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }
    
    @abstractmethod
    def get_fulfilment_info(self):
        pass

class CanBeShipped(ABC):

    @abstractmethod
    def calculate_shipping_cost(self):
        pass

class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.weight = weight

    def display_information(self):
        super().display_information()
        print("Weight:", self.weight, "kg")

    def get_fulfilment_info(self):
        return "This product requires physical shipping."

    def calculate_shipping_cost(self):
        return self.weight * 5

CanBeShipped.register(PhysicalProduct)

class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.download_size = download_size

    def display_information(self):
        super().display_information()
        print("Download size:", self.download_size, "MB")

    def get_fulfilment_info(self):
        return "This product is delivered digitally."
