#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 20230723 day1
        # 不行因为不是原地删除
        # nums=list(set(nums))
        # print(nums)
        # return len(nums)

        # j=0
        # n=len(nums)
        # for i in range(n):
        #     if i==0 or nums[j-1]!=nums[i]:
        #         nums[j]=nums[i]
        #         j+=1
        # return j

        j=0
        n=len(nums)
        for i in range(n):
            if i==0 or nums[j-1]!=nums[i]:
                # j 新的，i旧的
                nums[j]=nums[i]
                j+=1
        return j 



'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 指针 i 进行数组遍历
        n = len(nums)

        # 指针 j 指向即将被赋值的位置
        j = 0

        # 开始对数组进行遍历
        for  i in range(n): 

            # 进行筛选
            if  i == 0 or  nums[i] != nums[i - 1] : 
                # 赋值
                nums[j] = nums[i]

                # j 移动
                j += 1
 

        # 获取结果
        return j 
'''
# @lc code=end

