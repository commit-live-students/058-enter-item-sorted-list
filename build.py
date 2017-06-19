import bisect

def solution(list_of_nums, num):
    sorted_list = sorted(list_of_nums)
    bisect.insort(sorted_list,num)
    return sorted_list
