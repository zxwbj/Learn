
class A:

    def __init__(self, data='A'):
        self.data = data
        print("A: ", self.data)

    def say(self):
        print("A say")


class B(A):

    def __init__(self, data='B'):
        super().__init__(data)
        self.data = data
        print("B: ", self.data)

    def say(self):
        print("B say")


A().say()
B().say()
