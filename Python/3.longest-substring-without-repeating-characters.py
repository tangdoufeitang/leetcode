from __future__ import print_function

"""
3. Longest Substring Without Repeating Characters
DescriptionHintsSubmissionsDiscussSolution
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash = {}
        max_length = 0
        start = 0
        for i, string in enumerate(s):
        	# 当string再hash中且在start之后移动start
        	if string in hash and start <= hash[string]:
        		start = hash[string] + 1
        	else:
        		max_length = max(max_length, i - start + 1)
        	hash[string] = i

        return max_length


if __name__ == '__main__':
	print(Solution().lengthOfLongestSubstring('asdasfa'))