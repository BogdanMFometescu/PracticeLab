class Product:
    def __init__(self, product_id: int, product_name: str, price: float, quantity: int, is_available: bool):
        assert product_name.isspace() is False and product_name != "", f"{ValueError}" \
                                                                       f" Product should be a string!"
        assert price > 0, f"{ValueError} Product price must be greater than zero!"
        assert product_id > 0, f"{ValueError} Product Id must be greater than zero!"
        assert quantity > 0, f"{ValueError} Quantity must be greater than zero!"

        self._product_id = product_id
        self._product_name = product_name
        self._price = price
        self._quantity = quantity
        self._is_available = is_available

    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value

    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value: str):
        assert value.isspace() is False and value != "", f"{ValueError} Value cannot contain " \
                                                         f"string or whitespaces!"
        self._product_name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float):
        assert value > 0, f"{ValueError} Price must be a float number!"
        self._price = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value: int):
        self._quantity = value

    @property
    def is_available(self):
        return self._is_available

    @is_available.setter
    def is_available(self, value: bool):
        assert type(value) == bool, f"{ValueError} This must be  True or False"
        self._is_available = value

    def __repr__(self):
        return f" {self._product_id}, {self._product_name} , {self._price}, {self._quantity} , {self._is_available}"


class NewProduct(Product):
    def __init__(self, product_id: int, product_name: str, price: float, quantity: int, is_available: bool,
                 category: str, description: str):
        super().__init__(product_id, product_name, price, quantity, is_available)

        assert category.isspace() is False and category != "", f"{ValueError}" \
                                                               f" Category cannot contain empty" \
                                                               f" string or whitespaces!"

        assert description.isspace() is False and description != f"{ValueError} Description cannot be empty!"

        self.products_list = []
        self._category = category
        self._description = description

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value: str):
        self._category = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value: str):
        self._description = value

    def __repr__(self):
        return f"Product ID {self._product_id}" \
               f" Product Name :{self._product_name} " \
               f"Price: {self._price}" \
               f" Quantity : {self._quantity}," \
               f" Available : {self._is_available}," \
               f" Category : {self._category}," \
               f" Description :{self._description}, " \


    def add_product(self):
        self.products_list.append(self._product_id)
        self.products_list.append(self._product_name)
        self.products_list.append(self._price)
        self.products_list.append(self._quantity)
        self.products_list.append(self._is_available)
        self.products_list.append(self._category)
        self.products_list.append(self._description)

        return self.products_list
