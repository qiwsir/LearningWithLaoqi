#coding:utf-8

def get_by_index(lst, i, value=None):
    if i < len(lst):
        return lst[i]
    else:
        return value

if __name__ == "__main__":
    lst = ["python", "java", "c++"]
    result_2 = get_by_index(lst, 2)
    result_3 = get_by_index(lst, 3, "ruby")
    print("the list is: {0}".format(lst))
    print("index is 2, the result is {0}".format(result_2))
    print("index is 3, the result is {0}".format(result_3))
    
