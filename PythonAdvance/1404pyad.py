#coding:utf-8

def no_new_attributes(obj_setattr):
    def __setattr__(self, name, value):
        if hasattr(self, name):
            obj_setattr(self, name, value)
        else:
            raise AttributeError("can‘t add attribute {0} to {1}".format(name, self))
    return __setattr__

class NoNewAttrs:
    __setattr__ = no_new_attributes(object.__setattr__)

class Noclssattrs(type):    #元类
    __setattr__ = no_new_attributes(type.__setattr__)
    
class Person(NoNewAttrs, metaclass=Noclssattrs):
    firstname = ""
    lastname = ""
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __repr__(self):
        return "Person: {0}-{1}".format(self.firstname, self.lastname)

if __name__ == "__main__":
    #name = Person("qi", "wei")
    print(Person.firstname)

    print("-"*10)
    try:
        print("change the attribute of class.")
        Person.firstname = "laoqi"
        print(Person.firstname)
    except:
        print("you can not renew the attribute.")
    
    print("-"*10)
    try:
        print("add attribute for class.")
        Person.address = "soochow"
        print(Person.address)
    except AttributeError:
        print("can not add attribute for class.")