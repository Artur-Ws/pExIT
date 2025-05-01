import timeit
"""
Problem:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may not use the same element twice.
Return the answer as a list [i, j].

Example:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
# because nums[0] + nums[1] == 9
"""
# ------------------------ INPUT DATA ------------------------
nums1 = [4, 15, 32, 21, 11, 7, 29, 1, 22, 18,
         40, 5, 14, 31, 41, 33, 19, 20, 21, 3]
target1 = 31
correct1 = [4, 17]
# ------------------------- SOLUTION -------------------------
# --- brute force ---
# def solution(nums, target):
#     n = len(nums)
#     for i in range(n):
#         for j in range(i, n):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#     return 0


def solution(nums, target):
    component = {}
    for i, num in enumerate(nums):
        rem = target - num
        if rem in component:
            return [component[rem], i]
        else:
            component[num] = i



# -------------------------- TESTS ---------------------------
assert solution(nums1, target1) == correct1

