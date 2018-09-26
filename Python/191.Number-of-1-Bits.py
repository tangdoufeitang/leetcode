from __future__ import print_function

class Solution(object):
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