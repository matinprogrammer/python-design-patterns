"""
    Facade pattern
"""


class CPU:      # subsystem 1
    def execute(self):
        print("Executing CPU")


class Memory:   # subsystem 2
    def load(self):
        print("Loading data.")


class SSD:      # subsystem 3
    def read(self):
        print("Some data from ssd")


class Computer:     # Facade
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.ssd = SSD()

    def start(self):
        self.ssd.read()
        self.memory.load()
        self.cpu.execute()


def client_facade():
    computer = Computer()
    computer.start()


# Another implementation method
class Computer2:       # Facade 2
    def __init__(self, cpu_sub, memory_sub, ssd_sub):
        self.cpu = cpu_sub()
        self.memory = memory_sub()
        self.ssd = ssd_sub()

    def start(self):
        self.ssd.read()
        self.memory.load()
        self.cpu.execute()


def client_facade_2():
    computer = Computer2(CPU, Memory, SSD)
    computer.start()
