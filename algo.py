def test():
    print("Test")

def double(lst):
    res = ""

    for i in lst:
        res += i
        if i in "abcdefghijklmnopqrstuvwxyz":
            res += i
    return res 
