"""
    Visitor Pattern
"""
from abc import ABC, abstractmethod


class PublicVehicle(ABC):       # Abstract Element
    def __init__(self, dest):
        self.dest = dest

    @abstractmethod
    def order_ticket(self, ordering):
        pass


class Train(PublicVehicle):     # Concrete Element
    def order_ticket(self, ordering):
        ordering.train_ticket(self)


class Bus(PublicVehicle):       # Concrete Element
    def order_ticket(self, ordering):
        ordering.bus_ticket(self)


class Plane(PublicVehicle):     # Concrete Element
    def order_ticket(self, ordering):
        ordering.plane_ticket(self)


class Ticket(ABC):          # Abstract Visitor
    @abstractmethod
    def train_ticket(self, train):
        pass

    @abstractmethod
    def bus_ticket(self, bus):
        pass

    @abstractmethod
    def plane_ticket(self, plane):
        pass


class Order(Ticket):        # Concrete Visitor
    def train_ticket(self, train):
        print(f"This is a train ticket to {train.dest}")

    def bus_ticket(self, bus):
        print(f"This is a bus ticket to {bus.dest}")

    def plane_ticket(self, plane):
        print(f"This is a plane ticket to {plane.dest}")


order = Order()

t = Train("Mashhad")
t.order_ticket(order)

b = Bus("Tehran")
b.order_ticket(order)

p = Plane("Arak")
p.order_ticket(order)
