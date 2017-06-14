import bisect

def solution(list_of_nums, num):
    sort=sorted(list_of_nums)
    bisect.insort(sort,num)
    return sort
print solution([1, 2, 3, 5, 6], 4)
