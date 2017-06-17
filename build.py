import bisect

def solution(list_of_nums, num):
    """Below code is for the insertion of items in sorted order within a existing list"""
    bisect.insort(list_of_nums, num)
    list_of_nums.sort()
    print list_of_nums
    return list_of_nums

solution([1,2,5,4], 3)
