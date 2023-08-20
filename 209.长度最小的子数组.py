#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left,sum=0,0
        result=len(nums)+1
        for right in range(len(nums)):
            sum+=nums[right]
            while sum>=target:
                result=min(result,right-left+1)
                
                sum-=nums[left]
                left+=1
        return 0 if result==len(nums)+1 else result

'''
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 滑动窗口的左端
        left = 0

        # 滑动窗口中所有元素的和
        sum = 0

        # 记录滑动窗口的长度，并且不断更新获取最小的那个
        # 一开始，result 可以初始化为一个超过数组长度的值
        # 这样的目的是为了最后返回结果的时候判断 result 有没有被更新
        # 如果没有被更新，并且滑动窗口的长度不可能为 result，因为超过了数组的长度
        # 那就代表不存在符合条件的子数组，需要返回 0 
        # 比如 target = 11, nums = [1,1,1,1,1,1,1,1]
        # 先设置 result = 9，执行完后续代码，result 依旧为 9
        # 代表 nums 里面找不到一个子数组和大于等于 11 ，需要返回 0
        result = len(nums) + 1
        
        # 滑动窗口的右端从 0 开始，这样，当 nums 为空时，可以直接跳出 for 循环
        for right in range(len(nums)) :

            # 滑动窗口中加入了 nums[right] 这个元素
            # 滑动窗口元素和需要发生变化
            sum += nums[right]

            # 变化之后需要判断一下，如果滑动窗口的元素和大于等于了 target
            # 那么这个时候就需要不断的向右移动 left，缩小滑动窗口的长度
            while sum >= target : 
                
                # 在获取到一个满足要求的子数组时，更新 result 的值
                result = min(result, right - left + 1)

                # 把 nums[left] 移除滑动窗口
                sum -= nums[left]

                # 即 left 向右移动
                left += 1

      
        # 返回结果
        return 0 if result == len(nums) + 1 else result
'''
# @lc code=end

