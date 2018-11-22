from __future__ import print_function

# 42. Trapping Rain Water
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

# Example:

# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6

class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        result = 0

        while left < right:
        	if height[left] < height[right]:
        		left_max = max(left_max, height[left])
        		result += left_max - height[left]
        		left += 1
        	else:
        		right_max = max(right_max, height[right])
        		result += right_max - height[right]
        		right -= 1
        return result

if __name__ == '__main__':
	print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6