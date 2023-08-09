#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        xArray=list(str(x)) # 妙啊
        # xArray=str(x).split() # 这种就会有问题 why
        left=0
        right=len(xArray)-1

        while left<=right:
            if xArray[left]!=xArray[right]:
                return False
            left+=1
            right-=1

        return True



'''
class Solution:
    def isPalindrome(self, x: int) -> bool:

        # 转换为字符串数组的形式
        xArray = list(str(x))

        # 左边索引的位置在 0 
        left = 0

        # 右边索引的位置在 len(xArray) - 1
        right = len(xArray) - 1

        # 两个索引向内移动
        # left 向右移动
        # right 向左移动
        while left <= right:
            # 判断这两个元素值是否相同
            if xArray[left] != xArray[right]:
                # 如果不同，直接返回 False
                return  False

            # 否则，left 向右移动
            left += 1
        
            # right 向左移动
            right -= 1
         
         return True
'''
# @lc code=end

