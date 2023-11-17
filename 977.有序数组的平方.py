#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # l,r,k=0,len(nums)-1,len(nums)-1
        # result=[0]*len(nums)
        # # result=[float('inf')]*len(nums)

        # while l<=r:
        #     if nums[l]*nums[l]>nums[r]*nums[r]:
        #         result[k]=nums[l]*nums[l]
        #         l+=1
        #     else:
        #         result[k]=nums[r]*nums[r]
        #         r-=1
        #     k-=1
            
        # return result

        result=[0]*len(nums)
        l,r,k=0,len(nums)-1,len(nums)-1

        # 左闭右开,不行；越界nums[r]
        while l<=r:
            if nums[l]*nums[l]>nums[r]*nums[r]:
                result[k]=nums[l]*nums[l]
                l+=1
            else:
                result[k]=nums[r]*nums[r]
                r-=1
            k-=1
        return result

                
# @lc code=end

