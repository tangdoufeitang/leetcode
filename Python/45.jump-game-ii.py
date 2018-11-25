from __future__ import print_function

# 45. Jump Game II

# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Your goal is to reach the last index in the minimum number of jumps.

# Example:

# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
#     Jump 1 step from index 0 to 1, then 3 steps to the last index.

class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
        	return 0
        count = 0
        start = count = 0
        reach = nums[0]
        while start<len(nums) and start<=reach:
            count +=1
            if reach >= len(nums)-1:
                return count
            max_ = 0
            for i in range(start,reach+1):
                if i+nums[i]>max_:
                    max_ = i+nums[i]
                    start = i
            reach = max_
        return -1

if __name__ == '__main__':
	print(Solution().jump([1,4,5])) # 2