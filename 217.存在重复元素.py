#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
class Solution: 
    def containsDuplicate(self, nums: List[int]) -> bool:
        pre=set()
        for num in nums:
            if num in pre:
                return True
            pre.add(num)
        return False

'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 使用数据结构 set 来存放 nums 里面的所有数字
        pre = set()
        # 遍历数组 
        for num in nums:
            # 如果数字已经存在于 set 中，直接返回 true 
            if num in pre:
                return True
            # 把元素添加到 set 中
            pre.add(num)
        # 如果成功遍历完数组，则表示没有重复元素，返回 false
        return False
'''
# @lc code=end

