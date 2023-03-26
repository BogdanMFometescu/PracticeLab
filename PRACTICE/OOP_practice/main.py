
from item import Item

item1 = Item("MyItem", 750)
item1.name = "OtherItem"


item1.apply_discount()
item1.apply_increment(10)
print(item1.price)
print(item1.name)
