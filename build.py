import bisect
def solution(list_of_nums, num):
    print(list_of_nums)
    sorted_list = []
    sorted_list.extend([num])
    for i in list_of_nums:
        position = bisect.bisect(sorted_list, i)
        bisect.insort(sorted_list, i)
    return sorted_list
print solution([25, 45, 36, 47, 69, 48, 68, 78, 14, 37],[99])
