#
# @lc app=leetcode.cn id=1588 lang=python3
#
# [1588] 所有奇数长度子数组的和
#

# @lc code=start
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans=0
        # presum前缀和
        presum=[0]*(len(arr)+1)

        for i in range(len(arr)):
            presum[i+1]=presum[i]+arr[i]
        
        for i in range(len(arr)):
            # 这里len(arr)+1  需要包含长度len(arr)；cpp版的是<=所以没有+1的问题
            for j in range(1,len(arr)+1,2):
                if i+j-1<len(arr):
                    ans+=presum[i+j]-presum[i]
        return ans
# @lc code=end

