#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pos={}

        for i,v in enumerate(nums):
            if v in pos and i-pos[v]<=k:
                return True
            pos[v]=i
        return False
'''
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # 使用哈希集合
        pos = {}

        # 如果想在 for 循环中同时获得列表的索引 i 和元素值 v
        # 可以使用枚举内置函数 enumerate()
        for i, v in enumerate(nums):
            # 1、如果发现当前这个元素 v 已经存在于哈希集合里面
            # 说明在此之前就已经访问到了一个元素，值为 v
            # 2、pos[v] 表示的是之前访问到的元素值所在的索引
            # 判断 i - pos[v] <= k
            if v in pos and i - pos[v] <= k:
                # 符合要求，就返回 True
                return True
            # 否则，把 v 和 i 存储到哈希集合里面
            pos[v] = i

        # 最终没有找到，返回 False
        return False
'''
# @lc code=end

