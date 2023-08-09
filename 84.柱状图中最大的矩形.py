#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # res,stack=0,list()
        res,stack=0,[]
        newHeights = [0] * (len(heights) + 2 )
        newHeights[0]=0
        newHeights[len(newHeights)-1]=0
        # 搬过来
        for i in range(1,len(heights)+1):
            newHeights[i]=heights[i-1]

        for i in range(len(newHeights)):
            while stack and newHeights[i]<newHeights[stack[-1]]:
                cur=stack[-1]
                stack.pop() # 先存再弹

                curHeight=newHeights[cur]
                leftIndex=stack[-1]

                rightIndex=i
                curWidth = rightIndex - leftIndex - 1
                res=max(res,curWidth*curHeight)
            stack.append(i)
        return res
'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 初始化最终结果为0
        res = 0

        # 使用单调栈
        stack = list()


        # 将给定的原数组左右各添加一个元素0，方便处理
        newHeights = [0] * (len(heights) + 2 )

        # 左边界为 0 
        newHeights[0] = 0

        # 右边界边界为 0 
        newHeights[len(newHeights)-1] = 0

        # 其余不变
        for i in range( 1 ,len(heights) + 1 ) : 
            newHeights[i] = heights[i - 1]

                
        # 整体思路：
        # 对于一个高度，如果能得到向左和向右的边界
        # 那么就能对每个高度求一次面积
        # 遍历所有高度，即可得出最大面积
      
        # 开始遍历
        for i in range(len(newHeights)) : 
            # 如果栈不为空且当前考察的元素值小于栈顶元素值，
            # 则表示以栈顶元素值为高的矩形面积可以确定
            while stack  and newHeights[i] < newHeights[stack[-1]] : 
                # 弹出栈顶元素
                cur = stack[-1]

                stack.pop()

                # 获取栈顶元素对应的高
                curHeight = newHeights[cur]

                # 栈顶元素弹出后，新的栈顶元素就是其左侧边界
                leftIndex = stack[-1]

                # 右侧边界是当前考察的索引
                rightIndex = i
                # 计算矩形宽度
                curWidth = rightIndex - leftIndex - 1

                # 计算面积
                res = max(res, curWidth * curHeight)
            
            
            # 当前考察索引入栈
            stack.append(i)
        

        # 返回结果
        return res

'''
# @lc code=end

