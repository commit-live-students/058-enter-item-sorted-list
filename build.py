import bisect

def solution(list_of_nums, num):
    """Enter Code Here"""
    list_of_nums.sort()
    bisect.insort(list_of_nums,num)
    return list_of_nums
