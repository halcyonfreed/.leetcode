#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续 1 的个数
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        lastZero=-1 # slow指针 初值设为0！！
        ans=0
        for fast in range(len(nums)):
            # 不一定要用enumerate!!
            if nums[fast]==0:
                lastZero=fast
            else:
                ans=max(ans,fast-lastZero) # 更新ans值
        return ans
'''
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):

        # 最后一个 0 所在的索引位置
        lastZero = -1

        # 结果
        ans = 0

        # 从左到右访问数组 nums
        for i, num in enumerate(nums):

            # 1、当前元素为 0 ，更新 lastZero 
            if num == 0:
                lastZero = i
            
            # 2、否则说明当前元素为 1
            else:
                # 通过 lastZero 可以获取当前元素距离最前面的 1 的个数
                # 对比之前的 ans ，更新获取最大值
                ans = max(ans, i - lastZero)
        
        # 返回结果
        return ans
'''
# @lc code=end

