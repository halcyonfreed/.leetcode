#
# @lc app=leetcode.cn id=1475 lang=python3
#
# [1475] 商品折扣后的最终价格
#

# @lc code=start
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n=len(prices)
        ans=[0]*n
        stack=[]

        for i in range(n-1,-1,-1):
            p=prices[i]
            while stack and stack[-1]>p:
                stack.pop()

            if stack:
                ans[i]=p-stack[-1]
            else:
                ans[i]=p
            stack.append(p)
        return ans
'''
# 题目：LC1475. 商品折扣后的最终价格
# 难度：简单
# 作者：吴师兄学算法
# 算法：单调栈，时间复杂度O(N)
# 代码看不懂的地方，请直接在群上提问

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        # 原数组的长度
        n = len(prices)

        # 初始结果数组的内容，一开始都是 0 
        ans = [0] * n

        # 设置一个栈
        stack = []

        # 从后向前去遍历原数组 prices
        # 从后向前去填充 ans
        for i in range(n - 1, -1, -1):
            # 获取当前的原始价格
            p = prices[i]

            # 不断执行如下的逻辑
            # 1、栈不为空
            # 2、栈顶元素大于当前的价格
            # 使得栈中的元素都小于 p
            while stack and stack[-1] > p:
                # 弹出栈顶元素
                stack.pop()

            # 此时，对于 i 这个位置的价格来说
            # 在它的右侧小于 prices[i] 并且最靠近它的价格是 stack 的栈顶元素
            # 计算差值，获取答案 
            if stack:
                ans[i] = p - stack[-1]
            else:
                ans[i] = p

            # 再把当前的价格也压入栈
            # 栈是一个单调递减栈
            stack.append(p)

        # 返回答案  
        return ans

'''
# @lc code=end

