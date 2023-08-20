#
# @lc app=leetcode.cn id=852 lang=python3
#
# [852] 山脉数组的峰顶索引
#

# @lc code=start
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # # 我自己写的比答案好，他那个又臭又长
        # left,right=0,len(arr)-1
        # mid=left+(right-left)//2
        # # mid=(left+right)//2
        # # print(left,mid,right)
        # while left<right:
        #     mid=(left+right)//2
        #     if arr[mid]<arr[mid+1]:
        #         left=mid+1
        #     elif arr[mid]>arr[mid+1]:
        #         right=mid
        #         # print(left,mid,right)
        # return left

        # 答案very 差！！！
        left,right=1,len(arr)-2
        while left<right:
            mid=left+(right-left)//2
            if arr[mid]>arr[mid+1] and arr[mid]>arr[mid-1]:
                return mid
            if arr[mid]>arr[mid-1] and arr[mid]<arr[mid+1]:
                left=mid+1
            if arr[mid]<arr[mid-1] and arr[mid]>arr[mid+1]:
                right=mid-1
        return left
'''
# 登录 AlgoMooc 官网获取更多算法图解
# https://www.algomooc.com
# 作者：程序员吴师兄
# 代码有看不懂的地方一定要私聊咨询吴师兄呀
# 山脉数组的峰顶索引（ LeetCode 852 ）:https://leetcode-cn.com/problems/peak-index-in-a-mountain-array/
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        # 题目告诉我们 3 <= arr.length <= 10^4
        # 也就是说 arr 的最左侧和最右侧肯定不是山峰

        # 所以如果存在山脉，数组中最左侧的元素肯定不是山脉的山峰位置，因为它的左侧没有元素了
        # 因此，搜索区间需要从索引为 1 的位置开始
        left = 1

        # 同样的，如果存在山脉，数组中最右侧的元素肯定不是山脉的山峰位置，因为它的右侧没有元素了
        # 因此，搜索区间需要从索引为 nums.length - 2 的位置结束
        right = len(arr) - 2

        # 在 while 循环里面，left 不断的 ++，而 right 不断的 --
        # 当 left 和 right 相等， [ left , right ] 这个区间存在一个元素的时候
        # 这也意味着这个区间里面的元素找不到其它元素和它进行比较，它已经傲视群峰，就是山脉，得到结果
        # 所以，当 left == right 时，跳出循环
        # 此时，while 循环的判断不可以可以使用等号
        while left < right : 

            # left + (right - left) / 2 和 (left + right) / 2 的结果相同
            # 但是使用 left + (right - left) / 2 可以防止由于 left 、right 同时太大，导致相加的结果溢出的问题
            # 比如数据 int 的最大值为 2,147,483,647
            # 此时，left 为 2,147,483,640
            # 此时，right 为 2,147,483,646
            # 两者直接相加超过了 2,147,483,647，产生了溢出
            mid = left + (right - left) // 2

            # 由于题目中提示【题目数据保证 arr 是一个山脉数组】
            # 所以对于 arr 中任意位置的元素，比如 mid 所在的位置，只有以下三种情况

            # 1、mid 处于山峰位置，也就是它的值大于左侧，也大于右侧
            # arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1] 
            # 此时，找到了结果
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]  :
                
                # 返回结果
                return mid


            # 2、mid 处于上升状态，也就是它的值大于左侧，同时小于右侧
            # arr[mid] > arr[mid - 1] and arr[mid] < arr[mid + 1]
            # 那么，我们需要在右侧区间去寻找出下降的那段     
            if arr[mid] > arr[mid - 1] and arr[mid] < arr[mid + 1] :

                # 缩小区间，从 [ mid + 1 , right ] 里面去找
                left = mid + 1


            # 3、mid 处于下降状态，也就是它的值小于左侧，同时小于右侧
            # arr[mid] < arr[mid - 1] and arr[mid] > arr[mid + 1]
            # 那么，我们需要在左侧区间去寻找出上升的那段     
            if arr[mid] < arr[mid - 1] and arr[mid] > arr[mid + 1]   :

                # 缩小区间，从 [ left , mid - 1 ] 里面去找
                right = mid - 1


        # 跳出循环，此时 left == right，区间为 [ left，right ]，只有一个元素
        # 这也意味着这个区间里面的元素找不到其它元素和它进行比较，它已经傲视群峰，就是山脉，得到结果
        # 返回这个下标即可
        return left
'''
# @lc code=end

