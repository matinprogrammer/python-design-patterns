"""
    Iterator Pattern
"""
class Car:
    def __init__(self, name):
        self.name = name

class Garage:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def __iter__(self):
        return iter(self.cars)


if __name__ == '__main__':
    garage = Garage()
    garage.add_car(Car("Toyota"))
    garage.add_car(Car("BMW"))
    garage.add_car(Car("Benz"))

    for car in garage:
        print(f"car: {car.name}")
