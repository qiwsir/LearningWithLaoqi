#coding:utf-8

from collections import deque

class RingTube(deque):
    def __init__(self, size_max):
        super(RingTube, self).__init__()
        self.size_max = size_max

    def append(self, data):
        deque.append(self, data)
        if len(self) > self.size_max:
            self.popleft()

    def tolist(self):
        return list(self)

if __name__ == "__main__":
    x = RingTube(3)
    x.append("php")
    x.append("python")
    x.append("ruby")
    print(x.__class__, x.tolist())
    x.append("pascal")
    print(x.tolist())