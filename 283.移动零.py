#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        in_placen内嵌操作，原地修改！！
        """
        slow=0
        for fast in range(len(nums)):
            if nums[fast]!=0:
                nums[slow]=nums[fast]
                slow+=1
        for i in range(slow,len(nums)):
            nums[i]=0
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # 设置一个变量，用来指向经过一系列操作后数组中所有为 0 元素的第一个位置上
        # 一开始默认在索引为 0 的位置
        slow = 0

        # 从头到尾遍历数组
        # 遍历完毕之后，slow 指向了一个为 0 的元素，或者如果数组中不存在 0 ，就和 fast 一样，超过了数组的范围
        for fast in range(len(nums)) : 

            # 在遍历过程中，如果发现访问的元素是非 0 元素
            # 说明 slow 不在正确的位置上，需要向后移动，寻找合适的位置
            if nums[fast] != 0:

                # 这个时候，原先 slow 的值需要被 fast 的值覆盖
                nums[slow] = nums[fast]

                # slow 需要向后移动，寻找合适的位置
                slow += 1

        # 接下来，只需要把 slow 极其后面所有的元素都设置为 0 就行
        for i in range(slow,len(nums)) : 

            # 都设置为 0 
            nums[i] = 0
'''

# @lc code=end

