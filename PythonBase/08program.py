#coding:utf-8

class Person:
    def __init__(self, name):
        self.name = name
    
    def height(self, m):
        h = dict((["height", m],))
        return h
    
class Student(Person):
    def score(self, mark):
        result = {self.name: mark}
        return result

if __name__ == "__main__":
    tom = Student("Tom")
    print(tom.height(2.0))
    print(tom.score("A+"))