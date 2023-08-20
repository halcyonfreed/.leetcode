#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen=0
        hash=set()

        start=0
        # end是新增的
        for end in range(len(s)):
            while s[end] in hash:
                hash.remove(s[start])
                start+=1
            hash.add(s[end])
            maxLen=max(maxLen,end-start+1)
        return maxLen

'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 滑动窗口模板化解题，五步走策略

        # 【1、定义需要维护的变量】

        # 对于此题来说，要求是最大长度
        maxLen = 0

        # 同时又涉及去重，因此需要一个哈希表
        hash = set()

        # 【2、定义窗口的首尾端 (start, end)， 然后滑动窗口】

        # 窗口的左端位置从 0 开始
        start = 0

        # 窗口的右端位置从 0 开始，可以一直移动到尾部
        for end in range(len(s)) : 

            # 【3、更新需要维护的变量, 有的变量需要一个 if 语句来维护 (比如最大最小长度)】

            # 【4、如果题目的窗口长度可变: 这个时候一般涉及到窗口是否合法的问题】
            #  如果当前窗口不合法时, 用一个 while 去不断移动窗口左指针, 从而剔除非法元素直到窗口再次合法

            # 如果哈希表中存储了即将加入滑动窗口的元素
            while s[end] in hash : 
                
                # 那么需要不断的把窗口左边的元素移除窗口

                # 把 s.charAt(start) 移除记录
                hash.remove(s[start])

                # 窗口左端向右移动
                start += 1

            # 此时，滑动窗口可以接纳 s.charAt(end)
            hash.add(s[end])

            # 维护变量 maxLen
            maxLen = max(maxLen,end - start + 1)

        # 【5、返回所需要的答案】
        return maxLen
'''
# @lc code=end

