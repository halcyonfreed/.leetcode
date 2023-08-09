#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self.sums=[0]
        # _sums=self.sums # _代表内部变量 无法修改，这里不一定要内部变量，普通的即可
        

        for num in nums:
            self.sums.append(self.sums[-1]+num) # 求和的每个元素
            
    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right+1]-self.sums[left]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

