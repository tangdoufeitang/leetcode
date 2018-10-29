from __future__ import print_function

41. First Missing Positive

# Given an unsorted integer array, find the smallest missing positive integer.

# Example 1:

# Input: [1,2,0]
# Output: 3

# Example 2:

# Input: [3,4,-1,1]
# Output: 2

# Example 3:

# Input: [7,8,9,11,12]
# Output: 1
# Note:

# Your algorithm should run in O(n) time and uses constant extra space.

# 社区解法，暂时未看懂
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
        	if 0 <= nums[i] - 1 < len(nums) and nums[nums[i] - 1] != nums[i]:
        		temp = nums[i] - 1
        		nums[i], nums[temp] = nums[temp] = nums[i]
        for i in range(len(nums)):
        	if nums[i] != i + 1:
        		return i + 1
        return len(nums) + 1


if __name__ == '__main__':
	print(Solution().firstMissingPositive([3,4,-1,1]))