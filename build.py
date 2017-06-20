import bisect

def solution(list_of_nums, num):
    position = bisect.bisect_left(list_of_nums, num)
    bisect.insort(list_of_nums, num)
    return sorted(list_of_nums)
