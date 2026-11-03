
from product import PhysicalProduct, DigitalProduct, CanBeShipped

guitar = PhysicalProduct(101, "Guitar", 500, 10, 2.5)

print("=== PHYSICAL PRODUCT ===")
guitar.display_information()
print(guitar.get_fulfilment_info())
print("Shipping cost: $", guitar.calculate_shipping_cost())
print("Can be shipped:", isinstance(guitar, CanBeShipped))

game = DigitalProduct(102, "Computer Game", 50, 100, 1500)

print("\n=== DIGITAL PRODUCT ===")
game.display_information()
print(game.get_fulfilment_info())
print("Can be shipped:", isinstance(game, CanBeShipped))
