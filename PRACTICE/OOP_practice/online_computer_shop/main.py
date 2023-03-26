from product import NewProduct
from itertools import chain
import numpy as np
import pandas as pd


class ShopApp:
    def __init__(self):
        self.my_products = []
        self.df = None

    def products_details(self):
        # Create DataFrame from the list of products
        self.df = pd.DataFrame(self.my_products, columns=["Id",
                                                          "Product Name",
                                                          "Price",
                                                          "Quantity",
                                                          "Available",
                                                          "Category",
                                                          "Description"])
        print(self.df)

    def products_list(self):
        products_array = np.array(self.my_products)
        print(products_array[:, 1])

    def add_products_to_shop(self, product):
        self.my_products.append(product)

    def check_availability(self, product: str):
        # Check if the product is in, returns True or False
        result = product in chain(*self.my_products)
        if result:
            print(f"Product {product} is available in the shop!")
        else:
            print(f"Product {product} not available in shop!")

    def __repr__(self):
        return f"{self.my_products}"


if __name__ == "__main__":
    shop = ShopApp()
    computer = NewProduct(1, "Computer", 100, 1, True, "Hardware", "A small computer")
    monitor = NewProduct(2, "Monitor", 200, 1, True, "Hardware", "A small monitor")
    keyboard = NewProduct(3, "Keyboard", 300, 1, True, "Accessory", "A keyboard")
    shop.add_products_to_shop(computer.add_product())
    shop.add_products_to_shop(monitor.add_product())
    shop.add_products_to_shop(keyboard.add_product())
    shop.products_details()

