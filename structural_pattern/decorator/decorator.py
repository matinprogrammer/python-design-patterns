"""
    Decorator pattern
"""
import abc


class Page(abc.ABC):    # abstract component
    @abc.abstractmethod
    def show(self):
        pass


class AuthPage(Page):   # concrete component 1
    def show(self):
        print("welcome to authenticated page")


class AnonPage(Page):   # concrete component 2
    def show(self):
        print("welcome to anonymous page")


class PageDecorator(Page, abc.ABC):     # abstract decorator
    def __init__(self, component):
        self._component = component

    @abc.abstractmethod
    def show(self):
        pass


class PageAuthDecorator(PageDecorator):
    def show(self):
        username = input("enter your username: ")
        password = input("enter your password: ")
        if username == "admin" and password == "admin":
            self._component.show()
        else:
            print("you are not authenticated")


def client_decorator():
    page = AuthPage()
    authenticated = PageAuthDecorator(page)
    authenticated.show()


# usage:
# for get page without authenticated
# >>> AnonPage().show()
# for get page with authenticate
# >>> client_decorator()
