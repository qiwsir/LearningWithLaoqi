#coding:utf-8

class Price:
    def __init__(self):
        self.__price = 0
    
    def __get__(self, instance, owner):
        return self.__price
    
    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Price must be bigger than 0.")
        self.__price = value
    
    def __delete__(self, instance):
        del self.__price


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
    print(b1)