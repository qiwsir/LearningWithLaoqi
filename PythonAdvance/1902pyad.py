#coding:utf-8

def fibs():
    '''
    斐波那契数的无限生成器函数
    '''
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, prev + curr

if __name__ == "__main__":
    import itertools
    print(list(itertools.islice(fibs(), 10)))