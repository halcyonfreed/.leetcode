#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         slow=0
#         # fast找新数组元素，slow是新数组下标
#         for fast in range(len(nums)):
#             if nums[fast]!=val:
#                 nums[slow]=nums[fast]
#                 slow+=1
#             fast+=1
#         return slow
class Solution:
    def removeElement(self,nums:List[int],val:int)->int:
        slow=0
        for fast in range(len(nums)):
            if nums[fast]!=val:
                nums[slow]=nums[fast]
                slow+=1
            fast+=1
        return slow



# @lc code=end

