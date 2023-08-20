#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        # two-pointer + binary-search
        left,right=0 ,x
        ans=-1

        while left<=right:
            # 可以<=
            mid=(left+right)//2

            if mid*mid>x:
                right=mid-1
            else:
                left=mid+1
                ans=mid
        return ans

'''
class Solution:
    def mySqrt(self, x: int) -> int:
        # 需要寻找出一个数 ans ，使得 ans * ans <= x ，并且 ans 总是尽可能更大
        # 于是，开始在 [ 0  , x ] 这个区间中去查找
        # 在查找过程中，不断的去缩小区间
        
        # 左区间开始位置为 0 
        left = 0 
        
        # 右区间开始位置为 x
        right = x 
        
        # 算法平方根的结果，一开始为一个不可能的数 -1
        ans = -1

        # 开始在区间中查找
        while left <= right : 

            # 先定位中间元素
            mid = left + (right - left) // 2

            # 由于 x 的范围能到达 的最大值
            # 所以 mid 也有可能很大，导致 mid * mid 超过 的范围
            # 因此使用 long
            # 判断 mid 是否符合要求
            # 1、如果发现不够
            if  mid * mid <= x :

                # 保留结果
                ans = mid

                # 同时，可以舍去 left 左边的所有元素
                left = mid + 1
            
            # 2、如果发现超过
            else :
                # 同时，可以舍去 right 右边的所有元素
                right = mid - 1
 
        # 返回结果
        return ans
'''
# @lc code=end

