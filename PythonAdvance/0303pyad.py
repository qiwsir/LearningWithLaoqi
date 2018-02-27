# coding:utf-8

def contain_any_3(seq, aset):
    '''
    判断seq的字符是否在aset中
    '''
    return bool(aset.intersection(seq))

if __name__ == "__main__":
    seq = "apython"
    aset = set(['a', 'b', 'c', 'd', 'e'])
    result = contain_any_3(seq, aset)
    print(result)