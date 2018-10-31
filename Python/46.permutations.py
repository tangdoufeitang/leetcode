from __future__ import print_function

# 46. Permutations

# Given a collection of distinct integers, return all possible permutations.

# Example:

# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for n in nums:
            new_res = []
            for res in result:
                for i in range(len(res) + 1):
                    new_res.append(res[:i] + [n] + res[i:])
            result = new_res
        return result

if __name__ == '__main__':
	print(Solution().permute([1,2,3]))