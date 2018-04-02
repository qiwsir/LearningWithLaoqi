#coding:utf-8

import itertools

def windows(iterable, pre=1, post=1, padding=None):
    copies = itertools.tee(iterable, pre+1+post)    #对窗口中的每个元素产生一个迭代器
    pre_copies = copies[:pre]
    copy = copies[pre]
    post_copies = copies[pre+1:]
    #在元素之前的迭代器用填充值来填充开始部分
    pre_copies = [itertools.chain(itertools.repeat(padding, pre-i), itr) for i, itr in enumerate(pre_copies)]
    #在元素之后的迭代器切掉了开头并用填充值塞满末尾，不断重复
    post_copies = [itertools.chain(itertools.islice(itr, i+1, None), itertools.repeat(padding)) for i, itr in enumerate(post_copies)]
    print(pre_copies + list(copy) + post_copies)
    return pre_copies + list(copy) + post_copies

if __name__ == "__main__":
    seq = "123456789"
    windows(seq, 1, 2, 'x')
    #print("seq: ", seq)
    #print(list(r))