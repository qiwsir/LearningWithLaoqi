#coding:utf-8

def foo():
    def bar():
        print("bar is running")
    return bar

r = foo()
print(r)
r()