#coding:utf-8

def sort_dict_value(adict):
    keys = adict.keys()
    keys = sorted(keys)
    #return [ adict[k] for k in keys ]
    return map(adict.get, keys)

if __name__ == "__main__":
    d = {"lang":"python", "book":"learn python with laoqi", "publish":"phei"}
    print(d)
    #print(sort_dict_value(d))
    print(list(sort_dict_value(d)))