import random
from shop import Shop


class Product(Shop):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._product_name = None
        self._product_id = random.randint(1, 1000)

    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value

    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value




