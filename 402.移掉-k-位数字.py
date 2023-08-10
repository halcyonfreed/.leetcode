#
# @lc app=leetcode.cn id=402 lang=python3
#
# [402] 移掉 K 位数字
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for digit in num:
            while k and stack and stack[-1]>digit:
                stack.pop()
                k-=1
            stack.append(digit)
        return ''.join(stack[:len(stack)-k]).lstrip('0') or '0' 
    #lstrip() 方法用于截掉字符串左边的空格或指定字符; 最左边是0或就是0
'''
登录 AlgoMooc 官网获取更多算法图解
# https://www.algomooc.com
# 作者：程序员吴师兄
# 代码有看不懂的地方一定要私聊咨询吴师兄呀
# 移掉 K 位数字（ LeetCode 402 ）:https://leetcode-cn.com/problems/remove-k-digits/submissions/
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # 初始化栈，用来存储需要保留的数字
        stack = []
        
        # 从左到右遍历字符串 num
        for digit in num:
            
            # 如果此时
            # 1、栈不为空
            # 2、栈顶元素大于此时遍历的字符
            # 3、还没有删除足够多的数字，即 k > 0
            # 那么这个时候需要把栈顶元素弹出
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1

            # 把符合要求的字符放入到栈中
            stack.append(digit)

        return ''.join(stack[:len(stack) - k]).lstrip('0') or "0"
'''
# @lc code=end

