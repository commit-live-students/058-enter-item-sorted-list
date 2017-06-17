import bisect

def solution(list_of_nums, num):
    list_of_nums.sort()
    ins = bisect.bisect_left(list_of_nums,num,0,len(list_of_nums))
    list_of_nums.insert(ins,num)
    print list_of_nums
    return list_of_nums

solution([1,2,4],3)
