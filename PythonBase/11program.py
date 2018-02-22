#coding:utf-8

class ProtectMe:
    def __init__(self):
        self.me = "laoqi"
        self.__name = "qiwsir"

    def __python(self):
        print("I love python.")

    def code(self):
        print("Which lang do you like?")
        self.__python()

if __name__ == "__main__":
    p = ProtectMe()
    #print("p.me:", p.me)
    #print('p.__name:', p.__name)
    p.code()
    p.__python()