from __future__ import print_function

# 4. Median of Two Sorted Arrays

# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# You may assume nums1 and nums2 cannot be both empty.

# Example 1:

# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
# Example 2:

# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums.sort()
        length = len(nums)
        if length % 2:
        	n = nums[length // 2]
        else:
        	n = (nums[length // 2] + nums[(length // 2) - 1]) / 2
        return n

if __name__ == '__main__':
	print(Solution().findMedianSortedArrays([1, 3], [2]))