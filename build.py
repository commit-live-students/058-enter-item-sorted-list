import bisect

def solution(list_of_nums, num):
    list_of_nums.sort()
    bisect.insort(list_of_nums,num)
    return list_of_nums

print(solution([1, 2, 3, 5, 6], 4))    
