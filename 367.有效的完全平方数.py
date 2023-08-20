#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left,right=0,num
        while left<=right:
            mid=(left+right)//2

            if mid*mid>num:
                # mid大了
                right=mid-1
            elif mid*mid<num:
                left=mid+1
            else:
                return True
        return False
# @lc code=end

