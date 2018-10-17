from __future__ import print_function

# 28. Implement strStr()
# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:

# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:

# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Clarification:

# What should we return when needle is an empty string? This is a great question to ask during an interview.

# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
        	return 0
        else:
        	for i in range(len(haystack) - len(needle) + 1):
        		if haystack[i:i+len(needle)] == needle:
        			return i
        	return -1

if __name__ == '__main__':
	print(Solution().strStr('sfsaas', 'fs'))
