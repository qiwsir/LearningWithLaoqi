# coding:utf-8

"""
    This is my first program by Python.
    I am learning Python with Laoqi.
"""
print("Hello, World")
n = input("please input your age:")    # n is a str
if n.isnumeric():
    n = float(n)    # convert to float
    result = n + 100
    print("After 100 years, Your age is: ", result)
else:
    print("你不按照规则输入，所以不跟你玩了。")