import bisect

def solution(list_of_nums, num):
    """Enter Code Here"""
    l1 = sorted(list_of_nums)
    l1.append(num)
    l2 = sorted(l1)
    return l2
