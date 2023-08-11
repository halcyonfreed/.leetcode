#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans=nums[0]+nums[1]+nums[2]    

        for i in range(len(nums)):
            
            left=i+1
            right=len(nums)-1

            while left<right:
                sum=nums[i]+nums[left]+nums[right]
                if abs(target-sum)<abs(target-ans):
                    ans=sum
                if sum<target:
                    left+=1
                elif sum>target:
                    right-=1
                else:
                    return ans
        return ans

'''
# 登录 AlgoMooc 官网获取更多算法图解
# https://www.algomooc.com
# 作者：程序员吴师兄
# 代码有看不懂的地方一定要私聊咨询吴师兄呀
# 最接近的三数之和(16)：https://leetcode-cn.com/problems/3sum-closest/submissions/
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # 题目假定每组输入只存在恰好一个解，所以不需要处理边界情况
        ans = nums[0] + nums[1] + nums[2]

        # 先将数组进行排序操作，从小到大
        nums.sort()

        # 开始遍历整个数组
        # 在遍历的过程中，观察设置的三个位置的元素之后的大小
        # num[i] 为从左到右观察过去的元素
        # left 为从 i 到 len - 1 的元素
        # right 为从 len - 1 向左移动到 i 的元素
        for i in range(len(nums)) :

            # left 为从 i 到 len - 1 的元素，向右移动
            left = i + 1

            # right 为从 len - 1 向左移动到 i 的元素，向左移动
            right = len(nums) - 1

            # left 和 right 不断的向内移动
            while left < right :
                
                # 计算这三者之和
                sum = nums[i] + nums[left] + nums[right]

                # 寻找出更接近于 target 的那个和
                if abs(target - sum) < abs(target - ans) : 
                    ans = sum
                
                   
                # 如果三者之和小于 target ，那么说明需要找更大的数
                if sum < target :
                    # left 向右移动
                    left += 1

                # 如果三者之和大于 target ，那么说明需要找更小的数
                elif sum > target : 
                    # right 向左移动
                    right -= 1
                else : 
                    return ans
       
        # 返回结果   
        return ans
'''
# @lc code=end

