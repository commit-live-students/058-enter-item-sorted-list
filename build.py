import bisect

def solution(list_of_nums, num):
    sort_list = sorted(list_of_nums)
    bisect.insort(sort_list,num)
    return sort_list
