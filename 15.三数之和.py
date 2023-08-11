#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        if nums==None or len(nums)<3:
            return ans
        nums.sort()

        for i in range(len(nums)):
            if nums[i]>0:
                break # 没救了

            if i>0 and nums[i]==nums[i-1]:
                continue #重复

            left=i+1
            right=len(nums)-1 # 每次刷新初始位置

            while left<right:
                sum=nums[i]+nums[left]+nums[right]
                if sum==0:
                    # 找区间里所有的
                    ans.append([nums[i],nums[left],nums[right]])

                    while left<right and nums[left]==nums[left+1]:
                        # 可能left>right
                        left+=1
                    while left <right and nums[right]==nums[right-1]:
                        right-=1
                    left +=1
                    right-=1

                elif sum<0:
                    left+=1
                elif sum>0:
                    right-=1
        return ans


'''
# 登录 AlgoMooc 官网获取更多算法图解
# https://www.algomooc.com
# 作者：程序员吴师兄
# 代码有看不懂的地方一定要私聊咨询吴师兄呀
# 三数之和(15)：https://leetcode-cn.com/problems/3sum/ 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 题目存在多组解，每一组解都是一个数组，所以使用二维数组存储所有的解
        ans = []


        # 边界情况判断
        if nums == None or len(nums) < 3 :
           return ans

        # 先将数组进行排序操作，从小到大
        nums.sort()

        # 开始遍历整个数组
        # 在遍历的过程中，观察设置的三个位置的元素之后的大小
        # num[i] 为从左到右观察过去的元素
        # left 为从 i 到 len - 1 的元素
        # right 为从 len - 1 向左移动到 i 的元素
        for i in range(len(nums)) :

            # 如果发现 nums[i] > 0 ，由于 nums 是递增序列，left 在 nums[i] 的右侧，right 也在 nums[i] 的右侧
            # 那么 num[i]、nums[left]、nums[right] 都大于 0 
            # 说明这三数之和一定大于 0 ，结束循环
            if nums[i] > 0 : 
                break 

            # 答案中不可以包含重复的三元组，所以需要执行一个去重的操作
            # 比如这个输入 [-4,-1,-1,0,1,2]
            # i 指向的为第一个 -1 时，left 指向的元素值为 0 ，right 指向的元素值为 1 
            # i 指向的为第二个 -1 时，left 指向的元素值为 0 ，right 指向的元素值为 1 
            # 这两组解都是 [ -1 , 0 , 1]，所以需要去重
            if i > 0 and nums[i] == nums[ i - 1 ] :
               continue 

            # left 为从 i 到 len - 1 的元素，向右移动
            left = i + 1

            # right 为从 len - 1 向左移动到 i 的元素，向左移动
            right = len(nums) - 1

            # left 和 right 不断的向内移动
            while left < right :
                
                # 计算这三者之和
                sum = nums[i] + nums[left] + nums[right]
                
                # 发现三者之和为 0
                if sum == 0 :

                    # 把这个结果记录一下
                    ans.append([nums[i],nums[left],nums[right]])
            

                    # 答案中不可以包含重复的三元组，所以需要执行一个去重的操作
                    # 比如这个输入 [-2,0,0,2,2]
                    # i 指向的元素值为 -2 ，left 指向的元素值为第一个 0 ，right 指向的元素值为倒数第一个 2 时
                    # 它们的 sum 为 0 ，如果让 ，left 向右移动一下，，right 向左移动一下，它们的 sum 也为 0
                    # 但是这两组解都是 [ -2 , 0 , 2]，所以需要去重
                    while left < right and nums[left] == nums[ left + 1 ] :
                        # left 向右移动
                        left += 1
                    

                    while left < right and nums[right] == nums[ right - 1] :
                        # right 向左移动
                        right -= 1
                    

                    # left 向右移动
                    left += 1

                    # right 向左移动
                    right -= 1

                # 如果三者之和小于 0 ，那么说明需要找更大的数
                elif sum < 0 : 
                    # left 向右移动
                    left += 1

                # 如果三者之和大于 0 ，那么说明需要找更小的数
                elif sum > 0 : 
                    # right 向左移动
                     right -= 1
       
        # 返回结果   
        return ans
'''
# @lc code=end

