import bisect

def solution(list_of_nums, num):
    """Enter Code Here"""
    bisect.insort(list_of_nums, num)
    list_of_nums.sort()
    return list_of_nums

solution([1,2,5,4], 3)
