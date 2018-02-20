#coding:utf-8

def fibs(n):
    '''
    前n项的斐波那契数列，n表示数列长度
    '''
    r = [0, 1]
    for i in range(n-2):
        r.append(r[-1] + r[-2])
    return r

if __name__ == "__main__":
    f = fibs(10)
    print(f)