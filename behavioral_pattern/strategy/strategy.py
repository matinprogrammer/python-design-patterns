"""
    Strategy Pattern
"""
from abc import ABC, abstractmethod


class Read:     # Context
    def __init__(self, sentence):
        self._direction = None      # strategy instance
        self.sentence = sentence

    def set_direction(self, direction):     # set strategy
        self._direction = direction

    def read(self):
        return self._direction.direct(self.sentence)


class Direction(ABC):
    @abstractmethod
    def direct(self, data):
        pass


class Right(Direction):
    def direct(self, data):
        return data[::-1]


class Left(Direction):
    def direct(self, data):
        return data[:]


def client(sentence, direction):
    read = Read(sentence)
    read.set_direction(direction)
    print(read.read())


client("Hello World", Left())
client("Hello World", Right())
