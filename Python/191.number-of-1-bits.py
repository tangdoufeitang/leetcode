from __future__ import print_function

# 191.Number of 1 Bits
# Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

# Example 1:

# Input: 11
# Output: 3
# Explanation: Integer 11 has binary representation 00000000000000000000000000001011 
# Example 2:

# Input: 128
# Output: 1
# Explanation: Integer 128 has binary representation 00000000000000000000000010000000

class Solution:
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n:
        	n &= n - 1
        	result +=1
        return result

if __name__ == '__main__':
	print(Solution().hammingWeight(11))
