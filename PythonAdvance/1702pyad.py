#coding:utf-8

class MyMeta(type):
    def __new__(meta, name, bases, dct):
        print('-----------------------------------')
        print("Allocating memory for class", name)
        print(meta)
        print(bases)
        print(dct)
        return super(MyMeta, meta).__new__(meta, name, bases, dct)
    def __init__(cls, name, bases, dct):
        print('-----------------------------------')
        print("Initializing class", name)
        print(cls)
        print(bases)
        print(dct)
        super(MyMeta, cls).__init__(name, bases, dct)

class MyKlass(metaclass=MyMeta):
    def foo(self, param):
        pass
    barattr = 2

m = MyKlass()