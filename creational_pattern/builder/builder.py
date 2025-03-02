"""
    Builder pattern
"""
from abc import ABC, abstractmethod


class Wheel:
    size = None


class Body:
    shape = None


class Engine:
    hp = None


class Car:  # Product
    def __init__(self):
        self._wheel = None
        self._engine = None
        self._body = None

    def set_wheel(self, wheel):
        self._wheel = wheel

    def set_engine(self, engine):
        self._engine = engine

    def set_body(self, body):
        self._body = body

    def detail(self):
        print(f"Wheel: {self._wheel.size}")
        print(f"Engine: {self._engine.hp}")
        print(f"Body: {self._body.shape}")


class AbstractBuilder(ABC):  # abstract builder
    @abstractmethod
    def get_wheel(self): pass

    @abstractmethod
    def get_engine(self): pass

    @abstractmethod
    def get_body(self): pass


class Benz(AbstractBuilder):    # concrete builder
    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel

    def get_engine(self):
        engine = Engine()
        engine.hp = 500
        return engine

    def get_body(self):
        body = Body
        body.shape = "Suv"
        return body


class Bmw(AbstractBuilder):     # concrete builder
    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 20
        return wheel

    def get_engine(self):
        engine = Engine()
        engine.hp = 340
        return engine

    def get_body(self):
        body = Body
        body.shape = "Sedan"
        return body


class Director:
    _builder = None

    def set_builder(self, builder):
        self._builder = builder

    def construct(self):
        car = Car()

        wheel = self._builder.get_wheel()
        car.set_wheel(wheel)

        engine = self._builder.get_engine()
        car.set_engine(engine)

        body = self._builder.get_body()
        car.set_body(body)

        return car


def client_builder(builder):
    builders = {
        "bmw": Bmw,
        "benz": Benz
    }
    car = builders[builder]()

    director = Director()
    director.set_builder(car)
    result = director.construct()

    return result
