class Person:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f'Hello, my name is {self.name}')

p = Person('Matti')
p.hello()