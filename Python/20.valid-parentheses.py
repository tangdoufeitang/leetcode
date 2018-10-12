from __future__ import print_function

# 20. Valid Parentheses

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:

# Input: "()"
# Output: true
# Example 2:

# Input: "()[]{}"
# Output: true
# Example 3:

# Input: "(]"
# Output: false
# Example 4:

# Input: "([)]"
# Output: false
# Example 5:

# Input: "{[]}"
# Output: true

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack, lookup = [], {'}': '{', ')': '(', ']': '['}
        for i in s:
        	if i in lookup.values():
        		stack.append(i)
        	elif i in lookup.keys():
        		if len(stack) == 0 or lookup[i] != stack.pop():
        			return False
        	else:
        		return False
        return len(stack) == 0

    def isValid2(self, s):
    	lens, remainder = divmod(len(s), 2)
    	if remainder != 0:
    		return False
    	else:
    		for i in range(lens):
    			if '()' or '[]' or '{}' in s:
    				s = s.replace("()","")
    				s = s.replace("[]","")
    				s = s.replace("{}","")
    		if s:
    			return False
    		return True


if __name__ == '__main__':
	print(Solution().isValid('{}{}()'))