class Item:
    discount = 0.2
    all= []

    def __init__(self, name: str, price: float, qty: int= 1):
        assert price>0, f"Price {price}, should be greater than zero"
        assert qty>0, f"Quantity {qty}, should be greater than one"
        self.name = name
        self.price= price
        self.qty = qty
        Item.all.append(self)

    def get_cost(self):
        return self.price * self.qty

    def apply_discount(self):
        self.price = self.price * (1 - self.discount)


item1 = Item("Phone", 500,1)
item2 = Item("Laptop", 1000, 3)

print(f"Total cost of Phones before discount : {item1.get_cost()}")
print(f"Apply discount of: {item1.discount}")
item1.apply_discount()
print(f"cost after discount : {item1.get_cost()}")
#apply additional disount of 10%
item1.discount =  0.1
item1.apply_discount()
print(f"Cost after additional 10% discount :{item1.get_cost()}")
#new commit

#another new branch
