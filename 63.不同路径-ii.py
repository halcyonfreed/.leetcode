#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # # 0：初始化
        # m=len(obstacleGrid)
        # n=len(obstacleGrid[0])


        # # 特殊情况：起点 终点=1被占据，就没路可走
        # if obstacleGrid[m-1][n-1]==1 or obstacleGrid[0][0]==1:
        #     return 0
        # dp=[[0]*n for _ in range(m)]
        # for i in range(m):
        #     if obstacleGrid[i][0]==0:
        #         dp[i][0]=1
        #     else:
        #         break # 不用操作，就是保持原样，还是0
        # for j in range(n):
        #     if obstacleGrid[0][j]==0:
        #         dp[0][j]=1
        #     else:
        #         break
        

        # # 1 递推
        # for i in range(1,m):
        #     for j in range(1,n):
        #         # 多了下面两行
        #         if obstacleGrid[i][j]==1:
        #             continue
        #         dp[i][j]=dp[i-1][j]+dp[i][j-1]
        # return dp[m-1][n-1]
        m,n=len(obstacleGrid),len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1]==1 or obstacleGrid[0][0]==1:
            return 0
        
        dp=[[0]*n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0]==0:
                dp[i][0]=1
            else:
                break
        for j in range(n):
            if obstacleGrid[0][j]==0:
                dp[0][j]=1
            else:
                break
        
        for i in range(1,m):
            for j in range(1,n):

                # 写法一
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0 
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]

                # # 写法二
                # if obstacleGrid[i][j]==1:
                #     continue # 跳过for，dp[i][j]的赋值
                # dp[i][j]=dp[i-1][j]+dp[i][j-1]
                    
                
        return dp[m-1][n-1]



# @lc code=end

