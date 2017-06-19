import bisect
list_of_nums=[1, 2, 3, 5, 6]
num=4
def solution(list_of_nums, num):
    list_of_nums.sort()
    bisect.insort(list_of_nums,num)
    return list_of_nums
solution(list_of_nums, num)
