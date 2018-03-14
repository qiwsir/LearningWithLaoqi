#coding:utf-8

class NoNewAttrs:
    def __setattr__(self, name, value):
        if hasattr(self, name):
            object.__setattr__(self, name, value)
        else:
            raise AttributeError("can‘t add attribute {0} to {1}".format(name, self))

class Person(NoNewAttrs):
    firstname = ""
    lastname = ""
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __repr__(self):
        return "Person: {0}-{1}".format(self.firstname, self.lastname)

if __name__ == "__main__":
    name = Person("qi", "wei")
    print(name)

    print("-"*10)
    try:
        print("change the attribute of instance.")
        name.firstname = "laoqi"
        print(name)
    except:
        print("you can not renew the attribute.")
    
    print("-"*10)
    try:
        print("add attribute for instance.")
        name.address = "soochow"
        print(name.address)
    except AttributeError:
        print("can not add attribute for instance.")