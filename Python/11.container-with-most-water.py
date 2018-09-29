from __future__ import print_function

# 11.Container With Most Water
# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

# Note: You may not slant the container and n is at least 2.

# Example:

# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        l = 0
        r = len(height) - 1
        while l < r:
        # 	if height[l] < height[r]:
        # 		maxArea = max(maxArea, height[l] * (r - l))
        # 		l += 1
        # 	else:
        # 		maxArea = max(maxArea, height[r] * (r - l))
        # 		r -= 1
        # return maxArea
        	h = min(height[l], height[r])
        	max_area = max(max_area, h * (r - l))
        	while height[l] <= h and l < r: l += 1
        	while height[r] <= h and l < r: r -= 1

        return max_area

if __name__ == '__main__':
	print(Solution().maxArea([1,8,6,2,5,4,8,3,7])
        		
        
