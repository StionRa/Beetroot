class Car:
    total_number_cars = 0

    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.total_driven_km = 0
        Car.total_number_cars += 1

    def repaint(self, color):
        self.color = color

    def drive(self, km_driven):
        self.total_driven_km += km_driven

    def __repr__(self):
        return self.brand + ', ' + self.model + ', ' + str(self.year) + ', ' + self.color + ', ' + str(
            self.total_driven_km)

    def __str__(self):
        return self.brand + ', ' + self.model + ', ' + str(self.year)


class Truck(Car):
    def __init__(self, brand, model, year, color, trailers):
        super().__init__(brand, model, year, color)
        self.trailers = trailers

    def attach_trailers(self, num_of_trailers=1):
        self.trailers += num_of_trailers

    def detach_trailer(self, num_of_trailers=1):
        self.trailers -= num_of_trailers


my_truck = Truck('MAN', "TGX", 2012, 'black', 1)
print(my_truck)
print(repr(my_truck))
print(str(my_truck))