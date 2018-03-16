#coding:utf-8

class Test:
    _dict = {}
 
    def __new__(cls):
        """ class method """
        if 'key' in Test._dict:
            print("EXISTS")
            return Test._dict['key']
        else:
            print("NEW")
            return super(Test, cls).__new__(cls)
 
    def __init__(self):
        """ instance method """
        print("INIT")
        Test._dict['key'] = self
 
 
if __name__ == "__main__":
    t1 = Test()
    t2 = Test()