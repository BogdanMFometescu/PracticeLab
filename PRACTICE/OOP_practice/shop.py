import random


class Shop:
    def __init__(self, *args, **kwargs):
        self._shop_name = None
        self._shop_id = random.randint(1, 1000)

    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value

    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value

    def add_product(self):
        name = input("Enter name")