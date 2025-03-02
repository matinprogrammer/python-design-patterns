"""
    Interpreter Pattern
"""
from abc import ABC, abstractmethod


class Expression(ABC):
    @abstractmethod
    def interpret(self):
        pass

class Number(Expression):
    def __init__(self, value):
        self.value = int(value)

    def interpret(self):
        return self.value

class Add(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() + self.right.interpret()

class Subtract(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() - self.right.interpret()


def parse_expression(expression):
    tokens = expression.split()
    left = Number(tokens[0])
    operator = tokens[1]
    right = Number(tokens[2])

    if operator == '+':
        return Add(left, right)
    elif operator == '-':
        return Subtract(left, right)
    else:
        raise ValueError('عملگر پشتیبانی نمی‌شود')


if __name__ == '__main__':
    expressions = ['3 + 5', '10 - 2']
    for expr in expressions:
        interpreter = parse_expression(expr)
        result = interpreter.interpret()
        print(f"{expr} = {result}")
