#coding:utf-8

from collections import deque
import itertools

def windows(itertable, length=2, overlap=0):
    """
    length：窗口长度；
    overlap：重复的元素
    """
    it = iter(itertable)
    results = deque(itertools.islice(it, length))
    #results = list(itertools.islice(it, length))
    while len(results) == length:
        yield results
        for i in range(length-overlap):
            results.popleft()
        #results = results[lenght-overlap:]
        results.extend(itertools.islice(it, length-overlap))
    if results:
        yield results

if __name__ == "__main__":
    seq = "123456789"
    r = map("".join, windows(seq, length=3, overlap=1))
    print("seq: ", seq)
    print(list(r))
