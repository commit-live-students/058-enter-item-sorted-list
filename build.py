import bisect

def solution(list_of_nums, num):
    """Enter Code Here"""
    result = []
    result = sorted(list_of_nums)
    for i in result:
        if num > i and num < result[result.index(i)+1]:
            result.insert(result.index(i)+1,num)
    return result
