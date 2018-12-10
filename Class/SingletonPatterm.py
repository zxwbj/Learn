
class Singleton:

    _instance = None
    __init_flag = False

    def __init__(self):
        if Singleton.__init_flag:
            return None
        print("Singleton init ...")
        Singleton.__init_flag = True

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)

        return cls._instance


obj1 = Singleton()
obj2 = Singleton()
print(obj1, obj2)


# class Singleton:
#
#     def __init__(self):
#         print("__init__")
#
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(Singleton, "_instance"):
#             Singleton._instance = object.__new__(cls)
#         return Singleton._instance
#
#
# obj1 = Singleton()
# obj2 = Singleton()
# print(obj1, obj2)

