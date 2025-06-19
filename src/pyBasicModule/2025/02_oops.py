# =================== section-1 : abstraction

from abc import ABC, abstractmethod

class Animal(ABC):
    count = 0  # static field
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self): # Method Overriding
        print("Woof")

# =================== section-2 : overloading

from functools import singledispatchmethod

class Printer:
    @singledispatchmethod
    def print_data(self, data):
        print("Unsupported type")

    @print_data.register
    def _(self, data: int):
        print("Integer:", data)

    @print_data.register
    def _(self, data: str):
        print("String:", data)

    @print_data.register
    def _(self, data: list):
        print("List:", data)

p = Printer()
p.print_data(42)          # Integer: 42
p.print_data("hello")     # String: hello
p.print_data([1, 2, 3])   # List: [1, 2, 3]

# =================== section-3 :
