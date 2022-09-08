#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # """
        # Do not return anything, modify matrix in-place instead.
        # """

        Rows, Cols = len(matrix), len(matrix[0])
        RowZero = False

        for r in range(Rows):
            for c in range(Cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0

                if r > 0:
                    matrix[r][0]
                else:
                    RowZero = True
        
        for r in range(1,Rows):
            for c in range(1,Cols):
                if matrix[0][c] == 0 or matrix [r][0] ==0:
                    matrix[r][c] = 0

        if matrix[0][0]:
            for r in range(Rows):
                matrix[r][0] = 0
        
        if RowZero:
            for c in range(Cols):
                matrix[0][c] = 0
# @lc code=end

