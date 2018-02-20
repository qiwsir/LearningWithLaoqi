#coding:utf-8

class Person:
    """
    This is a simple of class.
    """

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return "-*-" + self.name + "-*-"

    def color(self, color):
        d = {}
        d[self.name] = color
        return d

if __name__ == "__main__":
    girl = Person("canglaoshi")
    print(girl.name)    #canglaoshi
    name = girl.get_name()
    print(name)         #-*-canglaoshi-*-
    her_color = girl.color("white")
    print(her_color)    #{'canglaoshi': 'white'}
