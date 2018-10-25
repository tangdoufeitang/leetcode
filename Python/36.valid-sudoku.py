from __future__ import print_function


# 判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。


# 上图是一个部分填充的有效的数独。

# 数独部分空格内已填入了数字，空白格用 '.' 表示。
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        big = set()
        for i in range(9):
        	for j in range(9):
        		if board[i][j] != '.':
        			cur = board[i][j]
        			if (i, cur) in big or (cur, j) in big or (i//3, j//3, cur) in big:
        				return False
        			big.add((i, cur))
        			big.add((cur, j))
        			big.add((i//3, j//3, cur))
        return True

if __name__ == '__main__':
	value = [[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]
	print(Solution().isValidSudoku(value))