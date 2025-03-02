"""
    Mediator Pattern
"""
from abc import ABC, abstractmethod


class AbstractMediator(ABC):
    @abstractmethod
    def notify(self, sender, event):
        pass


class ConcreteMediator(AbstractMediator):
    def __init__(self, sender_component, receiver_component):
        self.sender = sender_component
        self.sender.set_mediator(self)

        self.receiver = receiver_component
        self.receiver.set_mediator(self)

    def notify(self, sender, event):
        self.receiver.receive(sender, event)


class AbstractComponent(ABC):
    def __init__(self, mediator=None):
        self._mediator = mediator

    def set_mediator(self, mediator):
        self._mediator = mediator

    @abstractmethod
    def receive(self, sender, event):
        pass

    @abstractmethod
    def notify(self, event):
        pass


class ConcreteComponentA(AbstractComponent):
    def receive(self, sender, event):
        print(f"Component A received event ({event}) and sender is ({sender.__class__.__name__})")

    def notify(self, event):
        self._mediator.notify(self, event)

    def do_a(self):     # for example
        print('Component A does A.')
        self.notify("A")


class ConcreteComponentB(AbstractComponent):
    def receive(self, sender, event):
        print(f"Component B received event ({event}) and sender is ({sender.__class__.__name__})")

    def notify(self, event):
        self._mediator.notify(self, event)

    def do_b(self):  # for example
        print('Component B does B.')
        self.notify("B")


class ConcreteComponentC(AbstractComponent):
    def receive(self, sender, event):
        print(f"Component C received event ({event}) and sender is ({sender.__class__.__name__})")

    def notify(self, event):
        self._mediator.notify(self, event)

    def do_c(self):  # for example
        print('Component C does C.')
        self.notify("C")


component_a = ConcreteComponentA()
component_b = ConcreteComponentB()
component_c = ConcreteComponentC()

print("Example 1:")
mediator1 = ConcreteMediator(component_c, component_a)
component_c.do_c()

print("Example 2:")
mediator2 = ConcreteMediator(component_a, component_c)
component_a.do_a()

print("Example 3:")
mediator3 = ConcreteMediator(component_b, component_c)
component_b.do_b()
