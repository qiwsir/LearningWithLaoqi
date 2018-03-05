#coding:utf-8

def split_by(string, n, last_field=False):
    '''
    . string: the str to be split
    . n : the number of character in one part
    . last_field: include the last part
    '''
    pieces = [ string[k: k+n] for k in range(0, len(string), n)]
    if not last_field:    #delete the last element of pieces
        pieces.pop()
    return pieces

def split_at(string, cuts, last_field=False):
    '''
    . string: the str to be split
    . cuts: split the str before these points 
    . last_field: include the last part
    '''
    pieces = [ string[i: j] for i, j in zip([0]+cuts, cuts+[None])]
    if not last_field:
        pieces.pop()
    return pieces

if __name__ == "__main__":
    s = "learn python with Laoqi"
    s_by_6 = split_by(s, 6, last_field=True)
    print("split '{0}' by 6: {1}".format(s, s_by_6))
    print("-"*99)
    cuts = [3, 7, 12]
    s_cuts = split_at(s, cuts)
    print("split '{0}' at {1}, the result is:".format(s, cuts))
    print(s_cuts)