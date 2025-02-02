"""
    Proxy pattern
"""
from abc import ABC, abstractmethod
import time
import datetime


class AbstractServer(ABC):

    @abstractmethod
    def receive(self):
        pass


class Server(AbstractServer):
    def receive(self):
        print("Processing your request...")
        time.sleep(1)
        print("Done...")


class LogProxy(AbstractServer):
    def __init__(self, server: AbstractServer):
        self._server = server

    def logging(self):
        with open('log.log', 'a') as log:
            log.write(f"Request {datetime.datetime.now()} \n")

    def receive(self):
        self.logging()
        # ... another method
        self._server.receive()


def client_server(server, proxy):
    s = server()
    p = proxy(s)
    p.receive()


client_server(Server, LogProxy)     # example
