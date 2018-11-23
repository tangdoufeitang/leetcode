from __future__ import print_function

# 43. Multiply Strings

# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Example 1:

# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:

# Input: num1 = "123", num2 = "456"
# Output: "56088"
# Note:

# 1.The length of both num1 and num2 is < 110.
# 2.Both num1 and num2 contain only digits 0-9.
# 3.Both num1 and num2 do not contain any leading zero, except the number 0 itself.
# 4.You must not use any built-in BigInteger library or convert the inputs to integer directly.

class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1, num2 = num1[::-1], num2[::-1]
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                res[i + j] += int(num1[i]) * int(num2[j])
                res[i + j + 1] += res[i + j] / 10
                res[i + j] %= 10
                
        i = len(res) - 1
        while i > 0 and res[i] == 0:
            i -= 1

        return ''.join(map(str, res[i::-1]))

if __name__ == '__main__':
	print(Solution().multiply('2', '3')) # 6