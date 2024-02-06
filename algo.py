def test():
    print("Test")


def majority_element(nums: list[int]) -> int:
    """
    Boyer–Moore majority vote algorithm
    """
    c: int = 1
    el: int = nums[0]

    for i in range(1, len(nums)+1):
        if el == nums[i]:
            c += 1
        else:
            c -= 1
            if not c:
                el = nums[i]
                c = 1
    return el

def xyz():
    print(":)")


def double(lst):
    res = ""

    for i in lst:
        res += i
        if i in "abcdefghijklmnopqrstuvwxyz":
            res += i
    return res 

