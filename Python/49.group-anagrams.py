from __future__ import print_function

# 49. Group Anagrams

# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:

# All inputs will be in lowercase.
# The order of your output does not matter.

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dist = {}
        for i in strs:
        	item = tuple(sorted(i))
        	if dist.get(item) is None:
        		dist[item] = [i]
        	else:
        		dist[item].append(i)
        return [v for k, v in dist.items()]



if __name__ == '__main__':
	print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])) 
# [["tan","nat"],["bat"],["eat","tea","ate"]]