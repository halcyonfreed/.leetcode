#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

# @lc code=start
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         left,right=0,len(nums)-1

#         while left<=right:
#             # 也可以=不是<是<=
#             mid=left+(right-left)//2
#             if nums[mid]==target:
#                 return mid
#             elif nums[mid]<target:
#                 left=mid+1
#             else:
#                 right=mid-1
#         return -1

# 左闭右闭
# class Solution:
#     def search(self,nums:List[int],target:int)->int:
#         left,right=0,len(nums)-1
#         while(left<=right):
#             middle=(left+right)//2
#             if nums[middle]>target:
#                 right=middle-1
#             elif nums[middle]<target:
#                 left=middle+1
#             else:
#                 return middle
#         return -1

# 左闭右开
# class Solution:
#     def search(self,nums:List[int],target:int)->int:
#         # left,right=0,len(nums)-1 左闭右开初始值也要改，因为右边界不包括，所以right=len(nums)
#         left,right=0,len(nums)
#         while(left<right):
#             mid=(left+right)//2
#             if nums[mid]<target:
#                 left=mid+1
#             elif nums[mid]>target:
#                 right=mid
#             else:
#                 return mid
#         return -1

# class Solution:
#     def search(self,nums:List[int],target:int)->int:
#         # []
#         # left,right=0,len(nums)-1
#         # while left<=right:
#         #     middle=left+(right-left)//2
#         #     if nums[middle]>target:
#         #         right=middle-1
#         #     elif nums[middle]<target:
#         #         left=middle+1
#         #     else:
#         #         return middle
#         # return -1

#         # [)
#         left,right=0,len(nums)
#         while left<right:
#             middle=left+(right-left)//2
#             if nums[middle]>target:
#                 right=middle
#             elif nums[middle]<target:
#                 left=middle+1
#             else:
#                 return middle
#         return -1

'''
# 登录 AlgoMooc 官网获取更多算法图解
# https://www.algomooc.com
# 作者：程序员吴师兄
# 代码有看不懂的地方一定要私聊咨询吴师兄呀
# 二分查找(704):https://leetcode-cn.com/problems/binary-search/ 
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # 二分查找法的一种写法，在左闭右闭的区间里去查找目标值

        # left 为当前区间最左侧的元素，可以获取到
        left = 0

        # right 为当前区间最右侧的元素，可以获取到
        right = len(nums) - 1


        # 在 while 循环里面，left 不断的 ++，而 right 不断的 --
        # 当 [ left , right ] 这个区间不存在元素的时候，才跳出 while 循环，也就是当 left > right 时跳出循环
        # 即当 left = right + 1 时，搜索区间没有元素了
        # 由于 left 和 right 相遇的时候指向同一个元素，这个元素是存在于 [ left , right] 区间，这个区间就一个元素
        # 所以此时 while 循环的判断可以使用等号
        while left <= right :

            # left + (right - left) / 2 和 (left + right) / 2 的结果相同
            # 但是使用 left + (right - left) / 2 可以防止由于 left 、right 同时太大，导致相加的结果溢出的问题
            # 比如数据 int 的最大值为 2,147,483,647
            # 此时，left 为 2,147,483,640
            # 此时，right 为 2,147,483,646
            # 两者直接相加超过了 2,147,483,647，产生了溢出
            mid = left + (right - left) // 2

            # 中间的元素和目标值 target 相等，直接返回下标即可
            if nums[mid] == target :
                # 直接返回下标即可
                return mid
            
            # 中间的元素大于了目标值 target
            # 1、数组为有序数组，比如为递增数组
            # 2、数组中不存在重复元素
            # 由于该数组存在以上两个特点，所以 [ mid , right ] 这个区间中的所有元素都大于目标值 target
            # 因此，缩小查找区间为 [ left , mid - 1]
            elif nums[mid] > target :
                # 也就是说缩小之后的区间最右侧位置为 mid - 1
                right = mid - 1
            
            # 中间的元素小于了目标值 target
            # 1、数组为有序数组，比如为递增数组
            # 2、数组中不存在重复元素
            # 由于该数组存在以上两个特点，所以 [ left , mid ] 这个区间中的所有元素都小于目标值 target
            # 因此，缩小查找区间为 [ mid + 1 , right]
            elif nums[mid] < target : 
                # 也就是说缩小之后的区间最左侧位置为 mid + 1
                left = mid + 1
      
        
        # 查找完区间中的所有元素都没有找到，返回 -1
        return -1
'''

# class Solution:
#     def search(self,nums:List[int],target:int)->int:
#         # 左闭右开
#         left=0
#         right=len(nums) # 初值会错
#         while left<right:
#             mid=left+(right-left)//2
#             if target>nums[mid]:
#                 left=mid+1
#             elif nums[mid]>target:
#                 right=mid
#             else:
#                 return mid
#         return -1

class Solution:
    def search(self,nums:list[int],target:int)->int:
        # left=0
        # right=len(nums)
        # while left<right:
        #     mid=left+(right-left)//2
        #     if target>nums[mid]:
        #         left=mid+1
        #     elif target<nums[mid]:
        #         right=mid
        #     else:
        #         return mid
        # return -1

        # left=0
        # right=len(nums)-1
        # while left<=right:
        #     mid=left+(right-left)//2
        #     if nums[mid]>target:
        #         right=mid-1
        #     elif nums[mid]<target:
        #         left=mid+1
        #     else:
        #         return mid
        # return -1
        
        # # 左闭右开
        # left=0
        # right=len(nums)
        # while left<right:
        #     mid=left+(right-left)//2
        #     if nums[mid]<target:
        #         left=mid+1
        #     elif nums[mid]>target:
        #         right=mid
        #     else:
        #         return mid
        # return -1

        # 左闭右闭
        left=0
        right=len(nums)-1
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return -1


# @lc code=end

