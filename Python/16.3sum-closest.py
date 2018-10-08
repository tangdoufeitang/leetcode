from __future__ import print_function


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        diff = -1
        result = target
        for i in range(len(nums) - 2):
        	l, r = i + 1, len(nums) - 1
        	while l < r:
        		sums = nums[i] + nums[l] + nums[r]
        		if diff < 0 or diff > abs(sums - target):
        			diff = abs(sums - target)
        			result = sums
        		if sums < target:
        			l += 1
        		elif sums > target:
        			r -= 1
        		else: 
        			break
        return result
    def threeSumClosest2(self, nums, target):
    	num.sort()
        result = num[0] + num[1] + num[2]
        for i in range(len(num) - 2):
            j, k = i+1, len(num) - 1
            while j < k:
                sum = num[i] + num[j] + num[k]
                if sum == target:
                    return sum
                
                if abs(sum - target) < abs(result - target):
                    result = sum
                
                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
            
        return result

if __name__ == '__main__':
	print(Solution().threeSumClosest([-1,2,1,-4], 1))
        		