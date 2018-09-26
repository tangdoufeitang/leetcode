from __future__ import print_function


class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        while m < n:
        	n &= n - 1
        return n

if __name__ == '__main__':
	print(Solution().rangeBitwiseAnd(5, 7))
        	