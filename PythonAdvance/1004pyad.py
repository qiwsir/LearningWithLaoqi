#coding:utf-8

class CountWord(dict):
    def add(self, item, increment=1):
        self[item] = increment + self.get(item, 0)
    def sorts(self, reverse=False):
        lst = [ (self[k], k) for k in self ]
        lst.sort()
        if reverse:
            lst.reverse()
        return [(v, k) for k, v in lst]

if __name__ == "__main__":
    s = 'You raise me up, so I can stand on mountains,\
    You raise me up to walk on stormy seas,\
    I am strong when I am on your shoulders,\
    You raise me up to more than I can be.'
    words = s.split()
    c = CountWord()
    for word in words:
        c.add(word)
    print("从小到大")
    print(c.sorts())
    print("从大到小")
    print(c.sorts(reverse=True))