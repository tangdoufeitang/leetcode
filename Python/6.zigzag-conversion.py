from __future__ import print_function


# 6.ZigZag Conversion
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:

# P     I    N
# A   L S  I G
# Y A   H R
# P     I

# n=numRows
# Δ=2n-2    1                           2n-1                         4n-3
# Δ=        2                     2n-2  2n                    4n-4   4n-2
# Δ=        3               2n-3        2n+1              4n-5       .
# Δ=        .           .               .               .            .
# Δ=        .       n+2                 .           3n               .
# Δ=        n-1 n+1                     3n-3    3n-1                 5n-5
# Δ=2n-2    n                           3n-2                         5n-4

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        result = ""
        if numRows == 1:
        	return s
        length = len(s)
        for i in range(numRows):
        	step1, step2, pos = (numRows - i - 1) * 2, i * 2, i
        	if pos < length:
        		result += s[pos]
        	while 1:
        		pos += step1
        		if pos >= length:
        			break
        		if step1:
        			result += s[pos]
        		pos += step2
        		if pos >= length:
        			break
        		if step2:
        			result += s[pos]
        return result

# 这是耗时较短的答案

class Solution2:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        return ''.join(L)

if __name__ == '__main__':
	print(Solution().convert('sadadsafewqweqwdcsdd', 5))
