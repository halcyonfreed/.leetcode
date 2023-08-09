#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result=[]

        for token in tokens:
            if token in '+-*/':
                rightNum=result.pop()
                leftNum=result.pop()

                if token=='+':
                    ans=leftNum+rightNum
                elif token == "-":
                    ans = leftNum - rightNum
                elif token == "*":
                    ans = leftNum * rightNum
                elif token == "/":
                    ans = int(leftNum / rightNum)
            else:
                ans=int(token)
            result.append(ans)
        return result[-1]
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 使用一个列表作为栈，存储操作数，从左到右遍历逆波兰表达式
        result = []

        # 遍历字符串数组
        for token in tokens:
            # 如果是运算符
            if token in "+-*/":
                # 先出栈的是右操作数  最后最右是栈顶
                rightNum = result.pop()
                # 后出栈的是左操作数
                leftNum = result.pop()
                # 计算结果
                if token == "+":
                    ans = leftNum + rightNum
                elif token == "-":
                    ans = leftNum - rightNum
                elif token == "*":
                    ans = leftNum * rightNum
                elif token == "/":
                    ans = int(leftNum / rightNum)
            else:
                # 转换为数字
                ans = int(token)

            # 存储结果 再压回去
            result.append(ans)

        # 返回栈顶元素
        return result[-1]
'''
# @lc code=end

