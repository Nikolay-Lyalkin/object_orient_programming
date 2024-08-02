from src.product import Product


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):

        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"

        return product_str

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1


# pr1 = Product("apple", "green apple", 123, 12)
# pr2 = Product("apple", "green apple", 364, 65)
# # pr3 = Product("orange", "Afrika", 34, 980)
# x = Category("apple", "green apple", [pr1, pr2])
#
# print(x.name)
# print(x.description)
# print(x.products)
#
# pr3 = Product("orange", "Afrika", 34, 980)
# x.add_product(pr3)
#
# print(x.name)
# print(x.description)
# print(x.products)
#
# print(Category.product_count)
# print(Category.category_count)