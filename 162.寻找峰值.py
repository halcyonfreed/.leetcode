#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left,right=0,len(nums)-1
        while left<right:
            mid=left+(right-left)//2 # 防止left+right太大溢出

            if nums[mid]>nums[mid+1]:
                right=mid
            else:
                left=mid+1
        return left

'''
登录 AlgoMooc 官网获取更多算法图解
# https://www.algomooc.com
# 作者：程序员吴师兄
# 代码有看不懂的地方一定要私聊咨询吴师兄呀
# 寻找峰值(162):https://leetcode-cn.com/problems/find-peak-element/
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        # left 为当前区间最左侧的元素，可以获取到
        left = 0

        # right 为当前区间最右侧的元素，可以获取到
        right = len(nums) - 1


        # 在 while 循环里面，left 不断的 ++，而 right 不断的 --
        # 当 left 和 right 相等， [ left , right ] 这个区间存在一个元素的时候
        # 这也意味着这个区间里面的元素找不到其它元素和它进行比较，也就无法得知这个元素是否严格大于它左右相邻值的元素了
        # 所以，当 left == right 时，跳出循环
        # 此时，while 循环的判断不可以使用等号
        while left < right :

            # left + (right - left) / 2 和 (left + right) / 2 的结果相同
            # 但是使用 left + (right - left) / 2 可以防止由于 left 、right 同时太大，导致相加的结果溢出的问题
            # 比如数据 的最大值为 2,147,483,647
            # 此时，left 为 2,147,483,640
            # 此时，right 为 2,147,483,646
            # 两者直接相加超过了 2,147,483,647，产生了溢出
            mid = left + (right - left) // 2

            # 题目告诉我们 nums[-1] = nums[n] = -∞ 
            # 这暗示我们只要数组中存在一个元素比它相邻的元素大，那么沿着它一定可以找到一个峰值
            # 就像爬山一样，较小的山高度是 100，前面的山高度是 200，在前面是一个深渊，那么高度为 200 的那座山就是山峰
            # 所以比较 nums[mid] 与 nums[mid + 1] 的值

            # 如果 nums[mid] > nums[mid + 1]
            # 所以，如果存在山峰，那么这一段是右侧下降的那一段，因此需要在左侧去寻找上升的那段 
            if nums[mid] > nums[mid + 1] :

                # 缩小区间，从 [ left , mid ] 里面去找
                right = mid
            
            # 如果 nums[mid] < nums[mid + 1]
            # 所以，如果存在山峰，那么这一段是左侧上升的那一段，因此需要在右侧去寻找下降的那段         
            else :

                # 缩小区间，从 [ mid + 1 , right ] 里面去找
                left = mid + 1

        # 跳出循环，此时 left == right，返回这个下标即可
        return left
'''
# @lc code=end

