class Employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def give_raise(self, amount=5000):
        self.salary += amount
