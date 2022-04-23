    # [1,1,1,1,2,3,9]
    # mid point - 1 (3)
    # low = 0
    # high = 6
    # val -> = 1 

    # mid point = 3 (5)
    # low = 4
    # high = 6

    # mid point = 4 (2)
    # low = 4
    # high = 5


def binary_search(commit_list, target):
    if target is None:
        target = commit_list[0]
    low = 0
    high = len(commit_list) - 1

    while low < high:
        mid_point = (low + high) // 2
        if commit_list[mid_point] == target:
            low = mid_point 
        elif commit_list[mid_point] > target:
            high = mid_point - 1

    mid_point = (low + high) // 2
    return mid_point


#mock_data = [1,1,1,1,2,3,9]
mock_data = [1,1,1,1,1,3,9]
print(binary_search(mock_data, mock_data[0]))
x = binary_search(mock_data, mock_data[0])
print(mock_data[x:])
'''

def findRegression(commit_list):
    # iterate through the commit list and I am trying to find if a current commit is worse than the previous
    regression_list = []
    last_val = commit_list[0] 
    for i in range(1, len(commit_list) -1):
        is_worse = regressionChecker(last_val, commit_list[i])
        if is_worse:
            regression_list.append(commit_list[i])
        last_val = commit_list[i]
    return regression_list
'''
