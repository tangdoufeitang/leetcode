from __future__ import print_function

# 118. Pascal's Triangle

# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example:

# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        if numRows < 1:
        	return result

        for i in range(1, numRows + 1):
        	if i == 1:
        		array = [1]
        		result.append(array)
        	elif i == 2:
        		array = [1, 1]
        		result.append(array)
        		prev_list = array
        	else:
        		array = []
	        	for j in range(i):
	        		if j == i - 1 or j == 0:
	        			array.append(1)
	        		else:
	        			array.append(prev_list[j - 1] + prev_list[j])
	        	result.append(array)
	        	prev_list = array

        return result
# 更加简单的解法
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []
        for i in range(numRows):
            temp = [1] * (i + 1)
            ans.append(temp)
            for j in range(1,i):
                ans[i][j] = ans[i-1][j-1] + ans[i-1][j]
        return ans

if __name__ == '__main__':
	print(Solution().generate(0))
	print(Solution().generate(1))
	print(Solution().generate(2))
	print(Solution().generate(5))