class Detail:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def __add__(self, other):
        if isinstance(other, Detail):
            return self.cost + other.cost
        else:
            raise TypeError("Cannot add Detail object with non-Detail object")

detail1 = Detail("Dog", 10)
detail2 = Detail("Cat", 5)
total_cost = detail1 + detail2
print(total_cost)