#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res=[0,0]
        left,right=0,len(numbers)-1

        while left<right:
            if numbers[left]+numbers[right]==target:
                # 记录index号
                res[0]=left+1
                res[1]=right+1
                return res
            elif numbers[left]+numbers[right]<target:
                left+=1
            else:
                right-=1
        return res

'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # 初始结果数组
        res = [0, 0]

        # 定义左侧指针left，指向数组中第一个元素
        # 默认从数组的索引为 0 的位置开始
        left = 0

        # 定义右侧指针 right，指向数组中最后一个元素
        right = len(numbers) - 1

        # 两个索引向内移动
        # left 向右移动
        # right 向左移动
        while left < right:
            # 1、如果左侧指针与右侧指针所指向的元素和等于目标值，则返回结果
            if numbers[left] + numbers[right] == target:
                # 题目说明下标从 1 开始，就操作一下
                res[0] = left + 1

                res[1] = right + 1

                # 返回结果
                return res

            # 2、如果左侧指针与右侧指针所指向的元素和小于目标值
            elif numbers[left] + numbers[right] < target:

                # 因为数组是升序排列的，为了让两数之和变大一些
                # 因此应将左侧指针向右移动一位
                left += 1

            # 3、如果左侧指针与右侧指针所指向的元素和大于目标值
            elif numbers[left] + numbers[right] > target:

                # 因为数组是升序排列的，为了让两数之和变小一些
                # 因此应将右侧指针向左移动一位
                right -= 1

        # 返回结果
        return res
'''
# @lc code=end

