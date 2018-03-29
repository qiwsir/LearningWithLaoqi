#coding:utf-8
import itertools

def spliter(iterable, n):
    result = [ [] for x in range(n)]    #准备一个放置切片的列表
    resiter = itertools.cycle(result)    #无限长
    for item, sublist in zip(iterable, resiter):
        sublist.append(item)
    return result

if __name__ == "__main__":
    s = "abcde"
    print(spliter(s, 3))
    d = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8}
    print(spliter(d, 3))