#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump=list(range(len(nums)))
        for i in range(len(nums)):
            jump[i]=i+nums[i]

        index=0
        maxJump=jump[0]

        while index<len(nums) and index<=maxJump:
            if maxJump<jump[index]:
                maxJump=jump[index]
            
            index+=1
        
        if index>len(nums)-1:
            return True
        return False


'''
# 登录 AlgoMooc 官网获取更多算法图解
# https://www.algomooc.com
# 作者：程序员吴师兄
# 代码有看不懂的地方一定要私聊咨询吴师兄呀
# 跳跃游戏（ LeetCode 55 ）:https://leetcode-cn.com/problems/jump-game/submissions/
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 设置数组，保存每个位置如果在当前位置出发，一次性可以到达的最远位置
        # 比如 nums 为 [ 2 , 4 , 5 , 3 , 1 , 0 , 6]
        # 那么对于 2 来说，可以跳到最远的位置是 5 那个位置，即索引为 2 的那个位置
        # 对于 4 来说，可以跳到最远的位置是 0 那个位置，即索引为 5 的那个位置
        # 对于 5 来说，可以跳到最远的位置超过了数组的范围

        jump = list(range(len(nums)))

        # 初始化 jump
        for i in range(len(nums)) : 
            # jump[i] 就是当前的索引值 i 加上该位置可以跳跃的最大长度 nums[i]
            jump[i] = i + nums[i]
        

        # 从数组下标为 0 的位置开始起跳，索引为 0
        index = 0

        # 设置变量 maxJump，用来记录可以到达的最远位置
        # 从数组下标为 0 的位置开始起跳，此时记录的最远距离为 jump[0]
        maxJump = jump[0]

        # 开始起跳
        # 直到 index 到达数组尾部，index >= nums.length
        # 或者 index 超过 maxJump
        while index < len(nums) and index <= maxJump :
            
            # 如果发现可以跳到的最远距离 maxJump 小于 jump[index]
            if maxJump < jump[index] : 
                # 那么需要更新 maxJump
                maxJump = jump[index]
            

            # index 向前移动
            index += 1
        

        # 循环结束后，如果 index 已经访问了 nums 中所有的元素
        if index >len(nums) - 1 : 
            # 说明可以到达最后一个下标
            return True
        

        # 否则说明无法到达最后一个下标
        return False
'''
# @lc code=end

