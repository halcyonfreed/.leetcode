#
# @lc app=leetcode.cn id=1984 lang=python3
#
# [1984] 学生分数的最小差值
#

# @lc code=start
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # 先排序啊，我的天
        nums.sort() # 默认升序
        ans=nums[k-1]-nums[0]
        
        for right,num in enumerate(nums[k:],k):
            # 步长k
            ans=min(ans,num-nums[right-k+1])
            print(ans)
        return ans
'''
        # 题目：LC1984. 学生分数的最小差值
# 难度：简单
# 算法：固定滑窗


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # 贪心思想，对nums进行排序
        nums.sort()

        # 初始化第一个窗口的情况
        ans = nums[k-1] - nums[0]

        for right, num in enumerate(nums[k:], k):
            
            
            # 考虑每一个窗口中的情况
            # 窗口右边界为right，左边界为right-k+1
            # 更新ans
            ans = min(ans, num - nums[right-k+1])
        return ans
        '''      
# @lc code=end

