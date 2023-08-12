#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right=0,len(height)-1 # two-pointers双指针
        maxArea=0

        while left<right:
            w=right-left
            h=min(height[left],height[right])
            area=w*h

            if area>=maxArea:
                maxArea=area                

            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxArea

'''
# https://www.algomooc.com/587.html
# 作者：程序员吴师兄
# 代码有看不懂的地方一定要私聊咨询吴师兄呀
# 盛最多水的容器 ( LeetCode 11) : https://leetcode-cn.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: List[int]) -> int:
       # 设置两个索引，分别指向容器的两侧

       # 索引 left 指向最左边的柱子
       left = 0

       # 索引 right 指向最右边的柱子
       right = len(height) - 1

       # 设置一个变量用来保存当下水的最大面积
       res = 0

       # 移动 left 和 right，直到 left 和 right 相遇为止
       while left < right :

           # 水的宽度是 right - left
           width = right - left

           # 水的高度由两根柱子最短的那根决定
           h = min(height[left],height[right])

           # 计算此时水的面积
           area = width * h

           # 如果此时水的面积大于了我们之前保存的那个值，我们需要更新一下
           if area >= res :
               # 更新 res 的值为 area，确保 res 一直都是最大的值
               res = area
           
           # 接下来去观察需要移动哪根柱子：必定是最短的那根柱子

           # 如果左边的柱子更短，那么向内移动左边的柱子，因为只有这样，才有可能找到一个更高的水面
           # 在宽度一定变小的情况下，水的面积才有可能增大
           if height[left] < height[right] :
               # 向内移动左边的柱子
               left += 1

           # 如果右边的柱子更短，那么向内移动右边的柱子，因为只有这样，才有可能找到一个更高的水面
           # 在宽度一定变小的情况下，水的面积才有可能增大
           else:
               # 向内移动右边的柱子
               right -= 1
            
       # 最后返回最大的面积 res 即可
       return res
'''
# @lc code=end

