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
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__} ({self.name} , {self.price}, {self.quantity})"

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

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


class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(name, price, quantity)
        assert broken_phones >= 0, f"Broken Phones {broken_phones} should be greater than zero"

        self.broken_phones = broken_phones


phone1 = Phone("Apple", 500, 5)

print(Item.all)
print(Phone.all)
