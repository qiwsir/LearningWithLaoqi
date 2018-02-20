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

    def height(self, hig):
        r = super(Student, self).height(hig)
        return r
        #return "{0} is {1} meters in height".format(self.name, hig)

if __name__ == "__main__":
    tom = Student("Tom")
    print(tom.height(2.0))
    print(tom.score("A+"))