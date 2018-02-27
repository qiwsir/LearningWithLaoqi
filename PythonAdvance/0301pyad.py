# coding:utf-8

def contain_any_1(seq, aset):
    '''
    判断seq的字符是否在aset中
    '''
    for c in seq:
        if c in aset:
            return True
    return False

if __name__ == "__main__":
    seq = "apython"
    aset = set(['a', 'b', 'c', 'd', 'e'])
    result = contain_any_1(seq, aset)
    print(result)