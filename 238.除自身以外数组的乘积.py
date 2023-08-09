#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        answer=[1]*n # 初始乘积值

        for i in range(1,n):
            answer[i]=nums[i-1]*answer[i-1]
        

        right=1
        for i in reversed(range(0,n)):
            answer[i]=answer[i]*right
            right*=nums[i]
        return answer


# @lc code=end

