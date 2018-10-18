from __future__ import print_function

# 29. Divide Two Integers

# Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

# Return the quotient after dividing dividend by divisor.

# The integer division should truncate toward zero.

# Example 1:

# Input: dividend = 10, divisor = 3
# Output: 3
# Example 2:

# Input: dividend = 7, divisor = -3
# Output: -2
# Note:

# Both dividend and divisor will be 32-bit signed integers.
# The divisor will never be 0.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: 
# 	[−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.

class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        neg = ((dividend < 0) != (divisor < 0))
        dividend = dive = abs(dividend)
        divisor = divs = abs(divisor)
        ans = 0
        Q = 1
       	if dive < divs:
       		return 0
       	else:
       		while dive > divs:
       			dive -= divs
       			ans += Q
       			divs += divs
       			Q += Q
       			if dive < divs:
       				Q = 1
       				divs = divisor
       		if neg:
       			max(-ans, -2147483648)
       		else:
       			min(ans, 2147483647)

if __name__ == '__main__':
	print(Solution().divide(75,7))