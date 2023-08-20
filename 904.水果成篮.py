#
# @lc app=leetcode.cn id=904 lang=python3
#
# [904] 水果成篮
#

# @lc code=start
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans=0
        h=collections.Counter() # 是dict: 元素：次数

        left=0

        for right,x in enumerate(fruits):
            h[x]+=1 # 妙啊，元素作为Key！
            while len(h)==3:
                # 当有三个元素就右移了！！
                left_num=fruits[left]
                h[left_num]-=1 #往右移
                if h[left_num]==0:
                    del h[left_num]
                left+=1
            print(h)
            ans=max(ans,right-left+1)
        return ans
'''
# 题目：LC904. 水果成篮
# 难度：中等
# 算法：不定滑窗


# 本质是上求【元素种类为2的滑动窗口的最大长度】
# 故用哈希表Counter()维护窗口中元素种类及个数

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = 0
        h = collections.Counter()
        left = 0
        for right, x in enumerate(fruits):
            # Q1：对于每一个右指针right所指的元素x，做什么操作？
            # A1：将x加入哈希表中进行计数
            h[x] += 1
            # Q2：什么时候要令左指针left右移？在什么条件停止右移？【循环不变量】
            # A2：哈希表长度为3，说明滑动窗口中的元素种类多于2种
            # 此时需要令left右移，直到哈希表的长度为2
            while(len(h)==3):           # while的执行条件即为【循环不变量】
                left_num = fruits[left]
                h[left_num] -= 1
                if h[left_num] == 0:
                    del h[left_num]
                left += 1
            # Q3：什么时候进行ans的更新？
            # A3：cnt 的长度小于等于2时，更新 ans。
            ans = max(ans, right-left+1)
        return ans
'''
# @lc code=end

