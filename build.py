import bisect

def solution(list_of_nums, num):
    """Enter Code Here"""
    # position = bisect.bisect(list_of_nums.sort(), num)
    list_of_nums.sort()
    bisect.insort(list_of_nums, num)
    return list_of_nums
