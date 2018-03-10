#coding:utf-8

'''
问题：
有一个字符串，含有大小写的字母。要求对字符串中的字母进行排序，但不区分大小写。
'''

def sort_chr(string):
    return sorted(string, key=str.lower)

if __name__ == "__main__":
    s = "LifeisShorYouNeedPython"
    print(s)
    r = sort_chr(s)
    print(r)