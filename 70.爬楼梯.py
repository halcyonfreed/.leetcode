#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
    
        if n<=1:
            return n
        stairs=[1]*n
    
        stairs[0]=1
        stairs[1]=2

        for i in range(2,n):
            stairs[i]=stairs[i-1]+stairs[i-2]
        return stairs[n-1]


# @lc code=end

