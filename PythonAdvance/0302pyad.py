#coding:utf-8

def contain_any_2(seq, aset):
    '''
    判断seq的字符是否在aset中
    '''
    for item in filter(aset.__contains__, seq):
        return True
    return False

if __name__ == "__main__":
    seq = "python"
    aset = set(['a', 'b', 'c', 'd', 'e'])
    result = contain_any_2(seq, aset)
    print(result)