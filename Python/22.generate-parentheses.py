from __future__ import print_function

# 22. Generate Parentheses

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# For example, given n = 3, a solution set is:

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]


#  大神的答案
class Solution:
    def generateParenthesis(self, n):
	    def generate(p, left, right, parens=[]):
	        if left:         generate(p + '(', left-1, right)
	        if right > left: generate(p + ')', left, right-1)
	        if not right:    parens += p,
	        return parens
    return generate('', n, n)

    def generateParenthesis(self, n, open=0):
	    if n > 0 <= open:
	        return ['(' + p for p in self.generateParenthesis(n-1, open+1)] + \
	               [')' + p for p in self.generateParenthesis(n, open-1)]
    return [')' * open] * (not n)
    def generateParenthesis(self, n):
	    def generate(p, left, right):
	        if right >= left >= 0:
	            if not right:
	                yield p
	            for q in generate(p + '(', left-1, right): yield q
	            for q in generate(p + ')', left, right-1): yield q
    return list(generate('', n, n))


if __name__ == '__main__':
	print(Solution().generateParenthesis(5))