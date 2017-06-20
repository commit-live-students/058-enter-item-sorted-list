import bisect
def solution(list_of_nums, num):
    b=sorted(list_of_nums)
    a=bisect.bisect_left(b,num)
    b.insert(a,num)
    return b
