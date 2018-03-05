#coding:utf-8

print("Input two number; The program will print the result of division")
n1 = input("first number:")
n2 = input("second number:")

try:
    r = float(n1) / float(n2)
    
except ZeroDivisionError:
    print("n2 can not be 0")
except ValueError:
    print("you should input number")
else:
    print("{0} / {1} = {2}".format(n1, n2, r))
finally:
    print("Learn Python, U are right.")