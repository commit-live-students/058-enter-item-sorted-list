import bisect

def solution(list_of_nums, num):
    """Enter Code Here"""
    list_of_nums.append(num)
    list_of_nums.sort()
    return list_of_nums

lst = [1, 2, 3, 5, 6]
n = 4
print(solution(lst, n))
