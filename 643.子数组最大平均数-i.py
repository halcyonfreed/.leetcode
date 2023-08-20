#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sums=0
        largest=float('-inf')
        start=0
        
        for end in range(len(nums)):
            sums+=nums[end]
            if end-start+1==k:
                largest=max(largest,sums/k)

            # 右移
            if end>=k-1:
                sums-=nums[start]
                start+=1
        return largest
'''

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # 滑动窗口模板化解题，五步走策略

        # 【1、定义需要维护的变量】

        # 对于此题来说，需要维护当前滑动窗口的元素和、滑动过程中得出的最大平均数
        # 一开始，滑动窗口没有元素，元素和为 0 
        sums = 0

        # 由于数组存在负数，所以 largest 设置为一个最小值
        largest = float('-inf')

        # 【2、定义窗口的首尾端 (start, end)， 然后滑动窗口】

        # 窗口的左端位置从 0 开始
        start = 0

        # 窗口的右端位置从 0 开始，可以一直移动到尾部
        for end in range(len(nums)) : 

            # 【3、更新需要维护的变量, 有的变量需要一个 if 语句来维护 (比如最大最小长度)】

            # 维护元素和的值，窗口右端新增一个元素进来，元素和发生变化
            sums += nums[end]

            # if 语句
            # 如果窗口的长度为 k，需要计算平均数
            if end - start + 1 == k :

                # 维护 largest 变量
                largest = max( largest, sums / k )

            
            # 【4、如果题目的窗口长度固定：用一个 if 语句判断一下当前窗口长度是否达到了限定长度 】

            # 4.1、如果达到了，窗口左指针前移一个单位，从而保证下一次右指针右移时，窗口长度保持不变,
            if end >= k - 1 : 

                # 4.2、更新 (部分或所有) 维护变量 
                sums -= nums[start]
                
                # 4.3、窗口左指针前移一个单位保证下一次右指针右移时窗口长度保持不变
                start += 1
 
        # 【5、返回所需要的答案】
        return largest
'''
# @lc code=end

