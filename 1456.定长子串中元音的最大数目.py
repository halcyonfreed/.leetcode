#
# @lc app=leetcode.cn id=1456 lang=python3
#
# [1456] 定长子串中元音的最大数目
#

# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count=0
        vowels=['a','e','i','o','u']

        for ch in s[:k]:
            if ch in vowels:
                count+=1
        ans=count

        for end,ch in enumerate(s[k:],k):
            # end从k开始编号！！
            if ch in vowels:
                count+=1
        
            if s[end-k] in vowels:
                count-=1
            ans=max(ans,count)
        return ans
'''
# 题目：LC1456. 定长子串中元音的最大数目
# 难度：中等
# 算法：固定滑窗

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # 初始化包含所有5种元音字母的哈希集合
        vowels = {'a', 'e', 'i', 'o', 'u'}

        win_num = 0
        # 初始化第一个窗口的情况
        for ch in s[:k]:        
            if ch in vowels:
                win_num += 1
        
        ans = win_num

        for right, ch in enumerate(s[k:], k):
            # A1
            if ch in vowels:
                win_num += 1
            # A2
            left_ch = s[right-k]
            if left_ch in vowels:
                win_num -= 1
            # A3
            ans = max(ans, win_num)
        
        return ans
'''
# @lc code=end

