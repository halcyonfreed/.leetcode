#
# @lc app=leetcode.cn id=1695 lang=python3
#
# [1695] 删除子数组的最大得分
#

# @lc code=start
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        sums,largest=0,0
        hash=set()
        start=0

        for end in range(len(nums)):
            while nums[end] in hash:
                sums-=nums[start]
                hash.remove(nums[start])
                start+=1
            hash.add(nums[end])
            sums+=nums[end]
            largest=max(largest,sums)
        return largest
'''
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # 滑动窗口模板化解题，五步走策略

        # 【1、定义需要维护的变量】

        # 对于此题来说，需要维护当前滑动窗口的元素和、滑动过程中得出的最大得分
        # 一开始，滑动窗口没有元素，元素和为 0 
        sums = 0

        # 由于数组都是正数，所以可以初始化为 0
        largest = 0

        # 同时又涉及去重，因此需要一个哈希表
        hash = set()

        # 【2、定义窗口的首尾端 (start, end)， 然后滑动窗口】

        # 窗口的左端位置从 0 开始
        start = 0

        # 窗口的右端位置从 0 开始，可以一直移动到尾部
        for end in range(len(nums)) : 

            # 【3、更新需要维护的变量, 有的变量需要一个 if 语句来维护 (比如最大最小长度)】

            # 【4、如果题目的窗口长度可变: 这个时候一般涉及到窗口是否合法的问题】
            #  如果当前窗口不合法时, 用一个 while 去不断移动窗口左指针, 从而剔除非法元素直到窗口再次合法

            # 如果哈希表中存储了即将加入滑动窗口的元素
            while nums[end] in hash : 
                
                # 那么需要不断的把窗口左边的元素移除窗口

                # 元素和需要减去移除的值
                sums -= nums[start]

                # 把 nums[start] 移除记录
                hash.remove(nums[start])

                # 窗口左端向右移动
                start += 1

            # 此时，滑动窗口可以接纳 nums[end]
            hash.add(nums[end])

            # 维护变量 sum
            sums += nums[end]

            # 维护变量 largest
            largest = max(largest,sums)

        # 【5、返回所需要的答案】
        return largest
'''
# @lc code=end

