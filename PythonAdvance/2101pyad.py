#coding:utf-8

import heapq

def merge(*subseqs):
    h = []
    for subseq in subseqs:
        h.extend(subseq)
    heapq.heapify(h)
    while h:
        current_value = heapq.heappop(h)    #总删除最小的
        yield current_value

if __name__ == "__main__":
    a = [1,3,4]
    b = [2,5,8]
    r = merge(a, b)
    print("a:", a, "; b:", b)
    print("r:", list(r))
