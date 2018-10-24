from __future__ import print_function

# 33. Search in Rotated Sorted Array

# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

# Your algorithm's runtime complexity must be in the order of O(log n).

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
        	return -1
        l, r = 0, len(nums) - 1
        while l <= r:
        	mid =(l + r) // 2
        	if nums[mid] == target:
        		return mid
        	if (nums[l] < nums[mid] and nums[l] <= target < nums[mid]) or \
        		(nums[l] > nums[mid] and not (nums[mid] < target <= nums[r])):
        		r = mid - 1
        	else:
        		l = mid + 1
        return -1

class Solution2:
    # @param {integer[]} numss
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) / 2
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1



if __name__ == '__main__':
	print(Solution().search([4,5,7,8,9,0,1,3], 1))