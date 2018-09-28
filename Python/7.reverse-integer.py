from __future__ import print_function

# 7.
# Reverse Integer
# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x > 2 ** 31 - 1 or x < (-2) ** 31:
        	return 0
        f = x
        s = 0
        if x < 0:
        	x = -x
        while x > 0:
        	s *= 10
        	x, c = divmod(x, 10)
        	s += c

        if s > 2 ** 31 - 1 or s < (-2) ** 31:
        	return 0
        elif f > 0:
        	return s
        else:
        	return -s

if __name__ == '__main__':
	print(Solution().reverse(123))
        	