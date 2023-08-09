#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文串 II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(low,high):
            '''
            这个区间内是否是回文串
            '''
            left,right=low,high # 设两个指针指头尾
            while left<right:
                if s[left]!=s[right]:
                    return False
                else:
                    left+=1
                    right-=1
            return True
        
        
        low,high=0,len(s)-1
        while low<high:
            if s[low]==s[high]:
                low+=1
                high-=1
            else:
                return isPalindrome(low+1,high) or isPalindrome(low,high-1)
        return True

'''

class Solution:
    def validPalindrome(self, s: str) -> bool:

        # 判断 [ low , hight ] 这个区间的字符串是否是回文串
        def isPalindrome(low, high):

            # 左边索引的位置在 low 开始 
            left = low

            # 右边索引的位置在 high
            right = high

            # 两个索引向内移动
            # left 向右移动
            # right 向左移动
            while left < right:
                
                # 判断这两个元素值是否相同
                if s[left] != s[right]:
                    # 如果不同，直接返回 False
                    return False
                    
                # 否则，left 向右移动
                left += 1
                # right 向左移动
                right -= 1

            # 返回结果
            return True

        # 左边索引的位置在 0 开始 
        low = 0
        
        # 右边索引的位置在 len(s) - 1
        high = len(s) - 1

        # 两个索引向内移动
        # left 向右移动
        # right 向左移动
        while low < high:

            # 1、判断这两个元素值是否相同
            # 如果相同
            if s[low] == s[high]: 

                # 两个索引向内移动
                low += 1

                high -= 1

            # 2、如果不相同
            else:
                # 3、删除 low 所在这个元素，判断 [ low + 1 , high ] 是否是回文串
                # 或者
                # 4、删除 high 所在这个元素，判断 [ low  , high - 1 ] 是否是回文串
                return isPalindrome(low + 1, high) or isPalindrome(low, high - 1)
        
        # 返回结果
        return True
'''
# @lc code=end

