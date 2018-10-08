from __future__ import print_function

# Given a digit string, return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below.
#
# lookup = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
#
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:
# Although the above answer is in lexicographical order, your answer could be in any order you want.
#

# Iterative Solution

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        hash_map = {
        	'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        	'6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        length = len(digits)
        result = []
        if length == 0:
        	return []
        if length == 1:
        	return list(hash_map[digits[0]])
        prev = self.letterCombinations(digits[:-1])
        additional = hash_map(digits[-1])
        return [s + c for x in prev for c in additional]
    def letterCombinations2(self, digits):
    	"""
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
        	return []
        hash_map = {
        	'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        	'6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        res = [s for i in hash_map[digits[0]]]
        for i in digits[1:]:
        	res = [m + n for m in res for n in hash_map[i]]
        return res


class Solution2:
    letters = {"2": {"a","b","c"},
               "3": {"d","e","f"},
               "4": {"g","h","i"},
               "5": {"j","k","l"},
               "6": {"m","n","o"},
               "7": {"p", "q", "r", "s"},
               "8": {"t", "u", "v"},
               "9": {"w", "x", "y", "z"}}
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
               return []
        if len(digits) == 1:
            l = []
            for c in self.letters[digits[0]]:
               l.append(c)
            return l
        l = []
        for x in self.letters[digits[0]]:
            for c in self.letterCombinations(digits[1::]):
               l.append(x + c)
        return l


if __name__ == '__main__':
	print(Solution().letterCombinations('145654'))

        

