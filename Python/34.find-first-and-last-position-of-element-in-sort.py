from __future__ import print_function

# 34. Find First and Last Position of Element in Sorted Array

# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_len = len(nums)
        left = 0
        right = nums_len - 1
        if nums_len == 0 or target < nums[left] or target > nums[right]:
        	return [-1, -1]
        
        while left < right:
        	mid = left + (right - left)//2
        	if nums[mid] > target:
        		right = mid - 1
        	elif nums[mid] < target:
        		left = mid + 1
        	else:
        		if target > nums[left]:
        			left += 1
        		elif target < nums[right]:
        			right -= 1
        		else:
        			break
       	if nums[left] != target and nums[right] != target:
       		return [-1, -1]
        return [left, right]