
#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        names=path.split('/') # str->list
        stack=list()

        for name in names:
            print(name)
            if name=='..':
                if stack:
                    stack.pop()
            elif name and name!='.':
                stack.append(name)
        return "/"+'/'.join(stack)

'''
class Solution:
    def simplifyPath(self, path: str) -> str:

        # 分割字符串为列表形式
        names = path.split("/")

        # 利用栈来处理
        stack = list()

        # 访问列表里面的元素
        for name in names:
            print(name)
            # 1、如果是 .. 
            if name == "..":
                # 在栈不为空的情况下
                if stack:
                    # 弹出栈顶元素
                    stack.pop()
            # 2、如果是有效值
            # 字母
            elif name and name != ".":
                stack.append(name)
        # stack = ['Python', 'World', 'Hello']
        # new_string = '/ '.join(stack)
        # print(new_string)
        # 输出结果 Python/ World/ Hello
        # 我们使用/ 作为分隔符，将栈stack中的元素连接成一个新的字符串。
        # 每个元素之间使用/ 进行分隔，因此输出结果中每个元素都以/ 结尾（除了最后一个元素）。
        return "/" + "/".join(stack)
'''
# @lc code=end

