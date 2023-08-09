#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[0] * 9 for _ in range(9)]
        columns = [[0] * 9 for _ in range(9)]
        subboxes = [[[0] * 9 for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c != '.':
                    c = int(c) - 1
                    rows[i][c] += 1
                    columns[j][c] += 1
                    subboxes[int(i/3)][int(j/3)][c] += 1
                    if rows[i][c] > 1 or columns[j][c]>1 or subboxes[int(i/3)][int(j/3)][c]>1:
                        return False
        return True



'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 使用哈希表记录每一行每个数字出现的次数
        rows = [[0] * 9 for _ in range(9)]
        # 使用哈希表记录每一列每个数字出现的次数
        columns = [[0] * 9 for _ in range(9)]
        # 使用哈希表记录每一个【小九宫格】每个数字出现的次数
        subboxes = [[[0] * 9 for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c != '.':
                    c = int(c) - 1
                    rows[i][c] += 1
                    columns[j][c] += 1
                    subboxes[int(i/3)][int(j/3)][c] += 1
                    if rows[i][c] > 1 or columns[j][c]>1 or subboxes[int(i/3)][int(j/3)][c]>1:
                        return False
        return True
'''
# @lc code=end

