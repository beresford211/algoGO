'''
Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
'''

def pair_with_targetsum(arr, target_sum):
  # TODO: Write your code here
    if len(arr) < 2:
        return [-1, -1]

    p1 = 0
    p2 = len(arr) - 1 
    while (p1 < p2):
        current_sum = arr[p1] + arr[p2]
        if current_sum == target_sum:
            return [p1, p2]
        elif current_sum > target_sum:
            p2 -= 1
        elif current_sum < target_sum:
            p1 += 1
    return [-1, -1]

answer1 = pair_with_targetsum([1, 2, 3, 4, 6], 6)
answer2 = pair_with_targetsum([1, 2, 3, 4, 6], 6)
answer3 = pair_with_targetsum([1, 2, 3, 4, 6], 6)
