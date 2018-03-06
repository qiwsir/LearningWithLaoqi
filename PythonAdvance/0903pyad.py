#coding:utf-8

def get_by_index(lst, i, value=None):
    try:
        return lst[i]
    except IndexError:
        return value

if __name__ == "__main__":
    lst = ["python", "java", "c++"]
    result_3 = get_by_index(lst, -3)
    result_4 = get_by_index(lst, -4, "ruby")
    print("the list is: {0}".format(lst))
    print("index is -3, the result is {0}".format(result_3))
    print("index is -4, the result is {0}".format(result_4))
    