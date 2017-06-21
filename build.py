# Insert items into a list in sorted order
# https://app.commit.live/lesson/fsdse-python-assignment-58

# Define a function that takes two parameters: a list of numbers, a number
#The function should first sort the list and then insert the number into the list
#so that the list still remains sorted. Function should return the updated list.


a = [1, 10, 2, 20, 3, 30, 4, 40]

def solution(li_of_num, num):
    li_of_num.append(num)
    li_of_num.sort()
    return li_of_num

numb = 99

solution(a, numb)

#DOne, Not Posted =================================================================================
