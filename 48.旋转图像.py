#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix) 
        for i in range(n//2):
            for j in range(i,n-1-i):
                temp=matrix[i][j]
                # 与i,j相关的全部改了 [n-1-纵坐标][横坐标]
                matrix[i][j]=matrix[n-1-j][i]
                matrix[n-j-1][i]=matrix[n-1-i][n-j-1]
                matrix[n-i-1][n-j-1]=matrix[j][n-i-1]
                matrix[j][n-i-1]=temp
                



'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # 这是一个 n 行 n 列的矩阵
        n = len(matrix)

        # 只需要遍历 n / 2 行
        for i in range( n // 2 ) :
            
            # 每一列从 i 开始直到 n - i - 1
            for  j in range( i , n - i - 1 ) : 

                # 每一轮变化的过程是四个元素旋转
                temp = matrix[i][j]

                # 假设 matrix[i][j] 位于左上角的元素
                # 那么这个位置会被左下角元素替换，即 matrix[n - j - 1][i] 来到这个位置
                matrix[i][j] = matrix[n - j - 1][i]

                # 左下角元素被右下角的元素替换，即 matrix[n - i - 1][n - j - 1] 来到这个位置
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]

                # 右下角元素被右上角的元素替换，即 matrix[j][n - i - 1] 来到这个位置
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]

                # 右上角元素被左上角的元素替换，即 matrix[i][j] 来到这个位置
                matrix[j][n - i - 1] = temp
'''
# @lc code=end

