import csv


class Item:
    # Class attribute
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validation  to the received arguments
        assert type(name) == str, f"Name {name} should be a string!"
        assert price >= 0, f"Price {price} must be greater than zero "
        assert quantity >= 0, f"Quantity {quantity} should be greater than zero"

        # Assign to self Object
        self.__name = name  # private self.__name
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

        # Encapsulation

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    # Read only attribute
    @property
    def name(self):
        return self.__name

    # Can modify the value of attribute only based on this method
    @name.setter
    def name(self, value):
        self.__name = value

    def __repr__(self):
        return f"{self.__class__.__name__} ({self.name} , {self.__price}, {self.quantity})"

    def calculate_total_price(self):
        return self.__price * self.quantity

    @classmethod
    def instantiate_from_csv(cls):
        with open("Hotel Reservations.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item_x in items:
            print(item_x)

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
