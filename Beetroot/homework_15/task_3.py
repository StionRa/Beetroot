class Product:
    def __init__(self, name, price, amount, discount=0):
        self.name = name
        self.price = price
        self.amount = amount
        self.discount = discount

    def __str__(self):
        return f"{self.name}, amount {self.amount}, price {self.price}, discount {self.discount}%"

class ProductStore:
    def __init__(self):
        self.departments = []
        self.inventory = {}
        self.sales = 0

    def add_department(self, department_name):
        if department_name in self.departments:
            raise ValueError("Department already exists")
        self.departments.append(department_name)
        self.inventory[department_name] = {}
        return self

    def get_departments(self):
        return self.departments

    def add_product(self, department, product):
        if department not in self.departments:
            raise ValueError('Department does not exist')
        if not isinstance(product.amount, int) or product.amount <= 0:
            raise ValueError("Amount should be a positive integer")
        if product.name in self.inventory[department]:
            raise ValueError("Product already exists in department")
        self.inventory[department][product.name] = {'price': product.price, 'amount': product.amount, 'discount': product.discount}
        return f"{product.name}, amount {product.amount}, added successfully to {department} department"

    def get_products(self, department=None):
        if department:
            if department not in self.departments:
                raise ValueError('Department does not exist')
            return self.inventory[department]
        return self.inventory

    def product_info(self, name):
        for department in self.departments:
            if name in self.inventory[department]:
                return f'{name} in {department}: amount {self.inventory[department][name]["amount"]}, price {self.inventory[department][name]["price"]}'

    def get_income(self):
        return f"The store has an income: {self.sales}"

    def receive_shipment(self, name, amount):
        for department in self.departments:
            if name in self.inventory[department]:
                self.inventory[department][name]['amount'] += amount
                return f"Received {amount} units of {name} in {department} department"
        raise ValueError("Product does not exist in any department")

    def sell_product(self, name, amount):
        for department in self.departments:
            if name in self.inventory[department]:
                if self.inventory[department][name]['amount'] < amount:
                    raise ValueError('Not enough product in inventory')
                total = amount * self.inventory[department][name]['price'] - self.inventory[department][name]['discount']
                self.inventory[department][name]['amount'] -= amount
                self.sales += total
                return total
        raise ValueError("Product does not exist in any department")

    def discount(self, name, discount):
        for department in self.departments:
            if name in self.inventory[department]:
                current_price = self.inventory[department][name]['price']
                discounted_price = current_price * (1 - discount / 100)
                self.inventory[department][name]['price'] = discounted_price
                self.inventory[department][name]['discount'] = discount
                return f"Discount of {discount}% applied to {name}. New price: {discounted_price}"
        raise ValueError("Product not found")


store = ProductStore()
print(store.get_income())