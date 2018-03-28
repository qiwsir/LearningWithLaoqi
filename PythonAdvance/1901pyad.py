#coding:utf-8

import itertools

def frange(start, end=None, step=1.0):
    if end is None:
        end = float(start)
        start = 0.0
    assert step
    for i in itertools.count():
        next = start + i * step
        if (step>0.0 and next>=end) or (step<0.0 and next<=end):
            break
        yield next

if __name__ == "__main__":
    f = frange(1.2, 9)
    print(list(f))