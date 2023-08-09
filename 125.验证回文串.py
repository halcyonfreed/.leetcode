#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 设置左右两个指针
        left = 0 
        
        right = len(s) - 1 


        # 移动和观察者两个指针所指向元素之间的关系
        while left < right : 
            
            # 这里的逻辑有点像快速排序的代码

            # 如果 left 指向的元素不是字母、也不是数字
            # 那么可以忽略掉这个元素，即让 left 向右移动
            while  left < right and not s[left].isalnum():
                # left 向右移动
                left += 1

            

            # 如果 right 指向的元素不是字母、也不是数字
            # 那么可以忽略掉这个元素，即让 right 向左移动
            while left < right and not s[right].isalnum():
                # right 向左移动
                right -= 1

        

            # 来到这里时
            # 要么 left 和 right 相遇了，跳出循环
            # 要么 left 和 right 还没有相遇，并且它们都是指向字母或者数字
            if left < right :

                # 只需要判断一下 left 和 right 指向的元素值是否相同就行
                # 题目说明 可以忽略字母的大小写
                if s[left].lower() != s[right].lower():
                    # 不相同就直接说明不是回文串
                    return False
                

                # 否则，继续让两个指针向内移动

                # left 向右移动
                left += 1

                # right 向左移动
                right -= 1
    
        # 最后，没有得到 false 的答案就说明是回文串，返回 true
        return True
'''
# @lc code=end

