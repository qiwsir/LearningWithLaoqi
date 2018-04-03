#coding:utf-8

from weakref import WeakKeyDictionary

class Price:
    def __init__(self):
        #self.__price = 0
        self.default = 0
        self.values = WeakKeyDictionary()
    
    def __get__(self, instance, owner):
        # return self.__price
        return self.values.get(instance, self.default)
    
    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Price must be bigger than 0.")
        # self.__price = value
        self.values[instance] = value
    
    def __delete__(self, instance):
        # del self.__price
        del self.values[instance]


class Book:
    price = Price()

    def __init__(self, title, pages, price):
        self.title = title
        self.pages = pages
        self.price = price

    def __str__(self):
        return "{0} - {1}".format(self.title, self.price)

if __name__ == "__main__":
    b1 = Book("Django Practice", 263, 69)    
    b2 = Book("Start Python", 253, 59)
    print("b1 book price: ", b1.price)
    print("b2 book price: ", b2.price)
