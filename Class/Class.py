
class A:

    def __init__(self):
        print("A")

    def say(self):
        print("A say")


class B(A):

    def __init__(self, data='B'):
        super().__init__()
        A.__init__(self)
        self.data = data
        print("B: ", self.data)

    def say(self):
        print("B say")


A().say()
B().say()
