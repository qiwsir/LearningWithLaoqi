#coding:utf-8

class Test:
    def __init__(self):
        self._x = 0
    
    @property
    def x(self):
        print("get_x")
        return self._x
    @x.setter
    def x(self, value):
        print("set_x")
        self._x = value
    
    @x.deleter
    def x(self):
        print("del_x")
        del self.x
    #x = property(get_x, set_x, del_x, "I'm the 'x' property.")

t = Test()
print("t.x=", t.x)
t.x = 9
print("new t.x=", t.x)