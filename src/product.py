# from src.category import Category

class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, dict_product):
        # for product in category:
        #     if dict_product["name"] == product.name:
        #         product.quantity += dict_product["quantity"]
        #         if dict_product["price"] > product.price:
        #             product.price = dict_product["price"]
        return Product(**dict_product)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price_product):
        if price_product <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = price_product


# pr1 = Product("apple", "green apple", 13, 12)
# x = Category("apple", "green apple", [pr1])
# print(x.products)
# pr2 = Product.new_product({"name": "apple", "description": "green apple", "price": 13, "quantity": 12}, x.products)
# print(x.products)
# pr1.price = 0
# print(pr1.price)
