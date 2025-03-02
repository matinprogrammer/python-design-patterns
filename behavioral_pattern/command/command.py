"""
    Command Pattern
"""
from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class SimpleCommand(Command):
    def __init__(self, payload):
        self._payload = payload

    def execute(self):
        print(f"{self.__class__.__name__}: I can do simple thing lie printing({self._payload})")


class ComplexCommand(Command):
    def __init__(self, receiver, a, b):
        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self):
        print(f"{self.__class__.__name__}: complex stuff should be done a receiver object")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)


class Receiver:
    def do_something(self, a):
        print(f"{self.__class__.__name__}: working on ({a})")

    def do_something_else(self, b):
        print(f"{self.__class__.__name__}: working on ({b})")


class Invoker:
    _on_start = None
    _on_finish = None

    def set_on_start(self, command):
        self._on_start = command

    def set_on_finish(self, command):
        self._on_finish = command

    def operation(self):
        self._on_start.execute()
        self._on_finish.execute()


invoker = Invoker()
invoker.set_on_start(SimpleCommand("Say Hi!"))

receiver = Receiver()
invoker.set_on_finish(ComplexCommand(receiver, "Send Email", "Save report"))

invoker.operation()
