import bisect

def solution(list_of_nums, num):
    list_of_nums.sort()
    print list_of_nums
    bisect.insort(list_of_nums, num)
    return list_of_nums

solution([1, 2, 3, 5, 6], 4)
