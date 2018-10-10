from __future__ import print_function

# 18. 4Sum

# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

# Note:

# The solution set must not contain duplicate quadruplets.

# Example:

# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
    	def nsum(n, nums, target, result, results):
    		if n < 2 or len(nums) < n or target < nums[0] * n or target > nums[-1] * n:
    			return
    		if n == 2:
    			l, r = 0, len(nums)
    			while l < r:
    				if nums[l] + nums[r] > target:
    					r -= 1
    				elif nums[l] + nums[r] < target:
    					l += 1
    				else:
    					results.append(result + [nums[l], nums[r]])
    					l += 1
    					i -= 1
    					while l < r and nums[l] == nums[l - 1]: l += 1
    					while l < r and nums[r] == nums[r + 1]: r -= 1
    		else:
    			for i in range(len(nums) - n + 1):
    				if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
    					nsum(n - 1, nums[i + 1:], target - nums[i], result + [nums[i]], results)
    	results = []
    	nsum(4, nums, target, [], results)
    	return results
	# 改进版，别人的代码
   	def fourSum2(self, nums, target):
	    def findNsum(l, r, target, N, result, results):
	        if r-l+1 < N or N < 2 or target < nums[l]*N or target > nums[r]*N:  # early termination
	            return
	        if N == 2: # two pointers solve sorted 2-sum problem
	            while l < r:
	                s = nums[l] + nums[r]
	                if s == target:
	                    results.append(result + [nums[l], nums[r]])
	                    l += 1
	                    while l < r and nums[l] == nums[l-1]:
	                        l += 1
	                elif s < target:
	                    l += 1
	                else:
	                    r -= 1
	        else: # recursively reduce N
	            for i in range(l, r+1):
	                if i == l or (i > l and nums[i-1] != nums[i]):
	                    findNsum(i+1, r, target-nums[i], N-1, result+[nums[i]], results)

	    nums.sort()
	    results = []
	    findNsum(0, len(nums)-1, target, 4, [], results)
	    return results
	def fourSum3(self, nums, target):
        def nSum(nums, target, n, result, results):
            if len(nums) < n or n < 2 or n * nums[0] > target or n * nums[-1] < target:
                return []
            if n == 2:
                begin, end = 0, len(nums) - 1
                while begin < end:
                    sums = nums[begin] + nums[end]
                    if sums < target:
                        begin += 1
                    elif sums > target:
                        end -= 1
                    else:
                        plet = [nums[begin], nums[end]]
                        results.append(result + plet)
                        while begin < end and nums[begin] == plet[0]: begin += 1
                        while begin < end and nums[end] == plet[1]: end -= 1
            else:
                for i in range(len(nums) - n + 1):
                    if (i > 0 and nums[i] == nums[i - 1]) or (nums[i] + (n - 1) * nums[len(nums) - 1] < target):
                        continue
                    if n * nums[i] > target:
                        break
                    if n * nums[i] == target and i + n -1 < len(nums) and nums[i + n - 1] == nums[i]:
                        plet = [nums[i]] * n
                        results.append(result + plet)
                        break
                    nSum(nums[i + 1:], target - nums[i], n - 1, result + [nums[i]], results)

        results = []
        nums.sort()
        nSum(nums, target, 4, [], results)
        return results



if __name__ == '__main__':
	print(Solution().fourSum([1,0,-1,0,-2,2], 0))