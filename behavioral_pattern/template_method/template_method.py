"""
    Template Method Pattern
"""
from abc import ABC, abstractmethod


class Top(ABC):
    def template_method(self):
        self.first_common()
        self.second_common()
        self.third_require()
        self.fourth_require()

    def first_common(self):
        print("This is first common...")

    def second_common(self):
        print("This is second common...")

    @abstractmethod
    def third_require(self):
        pass

    @abstractmethod
    def fourth_require(self):
        pass


class One(Top):
    def third_require(self):
        print("This is third require from One")

    def fourth_require(self):
        print("This is fourth require from One")


class Two(Top):
    def second_common(self):
        print("This is second common from Two")

    def third_require(self):
        print("This is third require from Two")

    def fourth_require(self):
        print("This is fourth require from Two")


def client(klass):
    klass.template_method()


client(One())
client(Two())
