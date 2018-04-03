#coding:utf-8

class Book:
    def __init__(self, title, pages, price):
        self.title = title
        self.pages = pages
        if price<=0:
            raise ValueError("Price not allowed: {0}".format(price))
        self.price = price

    def __str__(self):
        return "{0} - {1}".format(self.title, self.price)

if __name__ == "__main__":
    b1 = Book("Django Practice", 263, -69)
    print(b1)