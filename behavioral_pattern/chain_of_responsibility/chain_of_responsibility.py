"""
    Chain of Responsibility Pattern
"""
from abc import ABC, abstractmethod


class AbstractHandler(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass


class BaseHandler(AbstractHandler):
    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class HandlerOne(BaseHandler):      # Concrete Handler
    def handle(self, request):
        if 0 <= request <= 10:
            print(f"{self.__class__.__name__} is processing this request {request}")
        else:
            return super().handle(request)


class HandlerTwo(BaseHandler):      # Concrete Handler
    def handle(self, request):
        if 10 < request <= 20:
            print(f"{self.__class__.__name__} is processing this request {request}")
        else:
            return super().handle(request)


class DefaultHandler(BaseHandler):      # Concrete Handler
    def handle(self, request):
        print(f"{self.__class__.__name__} is processing this request {request}")


def client(handler, request):
    for num in request:
        handler.handle(num)


numbs = [3, 14, 31, 9, 15, 5, 51, 90]
h_one = HandlerOne()
h_two = HandlerTwo()
h_default = DefaultHandler()

h_one.set_next(h_two).set_next(h_default)

client(h_one, numbs)
