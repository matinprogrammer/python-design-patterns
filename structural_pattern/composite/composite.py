"""
    Composite pattern
"""
from abc import ABC, abstractmethod


class Being(ABC):      # Abstract Component
    def add(self, child):
        pass

    def remove(self, child):
        pass

    def is_composite(self):
        return False

    @abstractmethod
    def execute(self):
        pass


class Animal(Being):    # Leaf
    def __init__(self, name):
        self.name = name

    def execute(self):
        print(f"Animal {self.name}")


class Human(Being):     # Concrete Composite
    def __init__(self):
        self._children = []

    def add(self, child):
        self._children.append(child)

    def remove(self, child):
        self._children.remove(child)

    def is_composite(self):
        return True

    def execute(self):
        print("Human Composite")
        for child in self._children:
            child.execute()


class Male(Human):      # Leaf
    def __init__(self, name):
        self.name = name

    def is_composite(self):
        return False

    def execute(self):
        print(f"\tMale {self.name}")


class Female(Human):  # Leaf
    def __init__(self, name):
        self.name = name

    def is_composite(self):
        return False

    def execute(self):
        print(f"\tFemale {self.name}")


def client_composite():
    f1 = Female("sara")
    f2 = Female("zahra")
    m1 = Male("john")

    h1 = Human()
    h1.add(f1)
    h1.add(f2)
    h1.add(m1)

    h1.execute()


client_composite()
