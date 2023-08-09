#
# @lc app=leetcode.cn id=1614 lang=python3
#
# [1614] 括号的最大嵌套深度
#

# @lc code=start
class Solution:
    def maxDepth(self, s: str) -> int:
        ans,size=0,0
        for c in s:
            if c=='(':
                size+=1
                ans=max(ans,size)
            elif c==')':
                size-=1
        return ans
'''
class Solution:
    def maxDepth(self, s: str) -> int:

        # size 表示栈的大小
        # ans 表示 size 的最大值，也就是最终的结果值
        ans, size = 0, 0

        # 遍历字符串 s
        for ch in s:
            # 如果遇到了一个左括号，将其入栈
            if ch == '(':
                # 栈中元素的个数加 1
                size += 1
                # 更新深度的值
                ans = max(ans, size)
            # 如果遇到了一个右括号，弹出栈顶的左括号
            elif ch == ')':
                # 栈中元素的个数减 1
                size -= 1
        # 返回最大值
        return ans
'''
# @lc code=end

