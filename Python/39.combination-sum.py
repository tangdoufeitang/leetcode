from __future__ import print_function

# 39. Combination Sum

# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

# The same repeated number may be chosen from candidates unlimited number of times.

# Note:

# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:

# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]
# Example 2:

# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.dfs(nums, target, 0, [], res)
        return res
    def dfs(self, nums, target, index, path, res):
    	if target < 0:
    		break;
    	if target == 0:
    		res.append(path)
    		return
    	for i in range(index, len(nums)):
    		self.dfs(nums, target - nums[i], i, path + [nums[i]], res)
 class Solution:
    def combinationSum(self, candidates, target):
      res = []
      candidates.sort()
      def dfs(remain, ele):
        if not remain: #当逐步相减至恰好为0的时候
          res.append(ele)
        else:
          for item in candidates: #每一次都对所有元素遍历，广度优先遍历
            if item > remain: #当前项大于剩余值时，循环停止
              break
            elif not ele or item >= ele[-1]:
              dfs(remain - item, ele + [item])
      dfs(target, [])
      return res

if __name__ == '__main__':
	print(Solution().combinationSum([2,3,6,7], 7))