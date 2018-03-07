#coding:utf-8

import re

def select_numbers(s):
    pieces = re.compile(r'(\d+)').split(s)    #convert string to str and number
    pieces[1::2] = map(int, pieces[1::2])     
    return pieces

def sort_filename(filename):
    return sorted(filename, key=select_numbers)

if __name__ == "__main__":
    files = ["py2.py", "py10.py", "py3.py"]
    result = sort_filename(files)
    print(files)
    print(result)