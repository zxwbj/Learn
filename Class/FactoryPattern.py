
class Factory:

    @staticmethod
    def create(name):
        if '宝马' == name:
            return BMW()
        if '大众' == name:
            return DZ()


class BMW:

    def __init__(self):
        print('Create 宝马')


class DZ:
    def __init__(self):
        print('Create 大众')


a = Factory.create("宝马")
b = Factory.create('大众')

