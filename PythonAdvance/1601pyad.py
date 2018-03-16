#coding:utf-8

class Singleton:
    _instance = None
    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)  
        return cls._instance  

class MyClass(Singleton):  
    a = 1

x = MyClass()
y = MyClass()

print(x)
print(y)