#coding:utf-8

class Temperature:
    coefficient = {"c": (1.0, 0.0, -273.15), "f": (1.8, -273.15, 32.0)}
    def __init__(self, **kargs):
        #判断参数是否在指定范围，否则报错
        assert set(kargs.keys()).intersection("kfcKFC"), "invalid arguments {0}".format(kargs)
        name, value = kargs.popitem()
        name = name.lower()
        setattr(self, name, float(value))

    def __getattr__(self, name):
        try:
            eq = self.coefficient[name.lower()]
        except KeyError:
            raise AttributeError(name)
        return (self.k + eq[1]) * eq[0] + eq[2]

    def __setattr__(self, name, value):
        name = name.lower()
        if name in self.coefficient:
            eq = self.coefficient[name]
            self.k = (value - eq[2]) / eq[0] - eq[1]
        elif name == 'k':
            object.__setattr__(self, name, value)
            #注意滴25行的写法，按照一般的理解，可以使用self.k=name或者setattr(self, name, value)
            #但是，如果这样，就意味着再次访问本函数，这样的结果是要无限循环下去
            #所以，用25行的写法
        else:
            raise AttributeError(name)
    
    def __str__(self):
        return "{0}K".format(self.k)

    def __repr__(self):
        return "Temperature(K={0}".format(self.k)

if __name__ == "__main__":
    t = Temperature(f=70)
    print("f=70, c=", t.c)
    t.c = 23
    print("c=23, f=", t.f)
        
        
            