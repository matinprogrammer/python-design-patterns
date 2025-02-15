"""
    Observer Pattern
"""
from abc import ABC, abstractmethod
from random import randrange


class Publisher(ABC):
    @abstractmethod
    def subscribe(self, observer):
        pass

    @abstractmethod
    def unsubscribe(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class ConcretePublisher(Publisher):
    _observers = []
    _state = None   # if this change publisher send signal to observers

    def subscribe(self, observer):
        self._observers.append(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notify(self):
        print("Notifying observers...")

        for observer in self._observers:
            observer.update(self)

    def operation(self):
        self._state = randrange(0, 10)
        print(f"state changed to {self._state}")
        self.notify()


class Observer(ABC):
    @abstractmethod
    def update(self, publisher):
        pass


class ConcreteObserverA(Observer):
    def update(self, publisher):
        if publisher._state <= 5:
            print("Observer A reacted to the event")


class ConcreteObserverB(Observer):
    def update(self, publisher):
        if publisher._state >= 5:
            print("Observer B reacted to the event")


publisher = ConcretePublisher()

observer_a = ConcreteObserverA()
observer_b = ConcreteObserverB()

publisher.subscribe(observer_a)
publisher.subscribe(observer_b)

publisher.operation()
