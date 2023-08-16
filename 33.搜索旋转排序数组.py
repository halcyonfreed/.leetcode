#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
        while left<=right:
            mid=left+(right-left)//2
            # mid=(left+right)//2

            if nums[mid]==target:
                return mid
            
            if nums[left]<=nums[mid]:
                if target>=nums[left] and target<=nums[mid]:
                    right=mid-1
                else:
                    left=mid+1

            else:
                if nums[right]>=target>=nums[mid]:
                    left=mid+1
                else:
                    right=mid-1
        return -1
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # left 指向当前区间的最左边位置，所以初始化为 0
        left = 0

        # right 指向当前区间的最右边位置，所以初始化为 len(nums) - 1
        right = len(nums) - 1

        # 循环进行二分查找，直到左端点位置超过了右端点
        # 或者在循环过程中找到了 target
        while left <= right:
            # 计算当前区间的中间位置，向下取整
            mid = (left + right) // 2

            # 如果中间位置数字 nums[mid] 等于目标值 target，那么说明找到了
            # 返回当前的下标 mid
            if nums[mid] == target:
                return mid

            # 否则的话需要先确定 mid 的左边还是右边为有序区间

            # 如果当前区间最左端的值 nums[left] 小于等于 nums[mid]
            # 说明从 left 到 mid 这段区间是递增的，为有序区间
            # 即 mid 的左侧为有序区间，右侧为无序区间
            if nums[left] <= nums[mid]:
                # 先去判断 target 是否在左侧有序区间内
                # 如果目标值 target 大于这段有序区间的最小值 nums[left] 同时小于这段有序区间的最大值 nums[mid]
                # 那么说明需要在这段有序区间去寻找 target 
                if target >= nums[left] and target <= nums[mid]:
                    # 所以缩小范围为 left 到 mid - 1
                    # 当前区间的左侧为 left，右侧 right = mid - 1
                    right = mid - 1
                # 否则说明需要在 mid 的右侧无序区间搜索
                else:
                    # 所以缩小范围为 mid + 1 到 right
                    # 当前区间的左侧为 left = mid + 1，右侧 right 
                    left = mid + 1

            # 否则说明当前区间最左端的值 nums[left] 大于 nums[mid]
            # 说明从 left 到 mid 这段区间是无序区间
            # 即 mid 的左侧为无序区间，右侧为有序区间 
            else:
                # 先去判断 target 是否在右侧有序区间内
                # 如果目标值 target 大于这段有序区间的最小值 nums[mid] 同时小于这段有序区间的最大值 nums[right]
                # 那么说明需要在这段有序区间去寻找 target 
                if target >= nums[mid] and target <= nums[right]:
                    # 所以缩小范围为 mid + 1 到 right
                    # 当前区间的左侧为 left = mid + 1，右侧 right 
                    left = mid + 1
                # 否则说明需要在 mid 的左侧无序区间搜索
                else:
                    # 所以缩小范围为 left 到 mid - 1
                    # 当前区间的左侧为 left，右侧 right = mid - 1
                    right = mid - 1

        # 目标值不存在，返回 -1
        return -1
'''
# @lc code=end

