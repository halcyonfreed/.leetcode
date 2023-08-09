#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除有序数组中的重复项 II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 做过类似的，和当前比
        slow =0
        for fast in range(len(nums)):
            # 分情况讨论
            if slow<2 or nums[fast]!=nums[slow-2]:
                nums[slow]=nums[fast]
                slow+=1
        return slow
# @lc code=end

