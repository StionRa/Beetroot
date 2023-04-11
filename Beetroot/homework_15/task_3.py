class Product:
    def __init__(self, type_product, name, price):
        self.type_product = type_product
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self):
        self.income = 0
        self.products = []

    def add(self, product, amount):
        if not isinstance(product, Product):
            raise ValueError("Invalid product type")
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("Amount should be a positive integer")
        product.price = 1.3
        self.products.append((product, amount))
        return f"{product.name}, amound {amount}, added success"

    def set_discount(self, identifier, percent, identifier_type='name'):
        if identifier_type not in ['name', 'type_product']:
            raise ValueError('Invalid identifier product type')
        if not isinstance(percent, int) or percent <= 0 or percent >= 100:
            raise ValueError("Percent should be a non-negative integer")
        for product, amount in self.products:
            if identifier_type == "name" and product.name == identifier:
                product.price *= (1 - percent / 100)
            elif identifier_type == "type_product" and product.type_product == identifier:
                product.price *= (1 - percent / 100)
        return f"for {identifier} discount is {percent}."

    def sell_product(self, product_name, amount):
        for i, (prod, count) in enumerate(self.products):
            if prod.name == product_name:
                if amount > count:
                    raise ValueError("Not enough products in stock")
                self.products[i] = (prod, count - amount)
                self.income = amount * prod.price
                return f"You have sell {amount} {product_name}, for {self.income}."
        raise ValueError("Product not found")

    def get_income(self, income):
        self.income = income
        return self.income

    def get_all_products(self):
        return [(product.name, product.type_product, product.price, amount) for product, amount in self.products]

    def get_product_info(self, product_name):
        for product, amount in self.products:
            if product.name == product_name:
                return f"We have in stock {product.name}, in amount {amount}"
        raise ValueError("Product not found")


p = Product('Sport', 'Football T-Shirt', 100)
x = Product("X", "XXX", 50)
p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()
print(s.add(p, 300))
print(s.add(x, 300))
print(s.add(p2, 300))

print(s.sell_product('Ramen', 100))

print(s.get_product_info('Ramen'))
print(s.set_discount("XXX", 10))
print(s.sell_product("XXX", 100))

print(s.get_all_products())