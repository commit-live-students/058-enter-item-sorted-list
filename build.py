import bisect

def solution(list_of_nums, num):
     list_of_nums.append(num)
     new_list=sorted(list_of_nums)
     return new_list
