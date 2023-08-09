#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        if len(pattern)!=len(s):
            return False
        
        t=pattern
        dic1,dic2={},{}
        for i in range(len(pattern)):
            if s[i] in dic1 and dic1[s[i]]!=t[i]:
                return False
            
            if t[i] in dic2 and dic2[t[i]]!=s[i]:
                return False
            
            if s[i] not in dic1:
                dic1[s[i]]=t[i]
            if t[i] not in dic2:
                dic2[t[i]]=s[i]
        
        return True


'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        s = s.split()

        if len(pattern) != len(s):
            return False
        
        t = pattern

        # 接下来的逻辑和 LC205. 同构字符串 一模一样
        
        # 设置一个哈希集合用来存储字符串 s 当中的元素
        dic1 = {}

        # 设置一个哈希集合用来存储字符串 t 当中的元素
        dic2 = {}

        

        # 由于 t.length == s.length
        # 按照顺序访问 s 和 t 中对应的元素
        for i in range(len(pattern)):

            # 1、访问的元素 s[i] 存在于 dic1 中
            # 并且发现它对应的元素值和当前 t 中元素 t[i] 不相同
            # 返回 False
            if s[i] in dic1 and dic1[s[i]] != t[i]:
                return False

            # 2、访问的元素 t[i] 存在于 dic2 中
            # 并且发现它对应的元素值和当前 s 中元素 s[i] 不相同
            # 返回 False
            if t[i] in dic2 and dic2[t[i]] != s[i]:
                return False

            # 3、访问的元素 s[i] 不存在于 dic1 中
            # 存放到哈希集合中
            if s[i] not in dic1:
                # dic1[s[i]] = t[i]
                dic1[s[i]] = t[i]

            # 3、访问的元素 t[i] 不存在于 dic2 中
            # 存放到哈希集合中
            if t[i] not in dic2:
                # dic2[t[i]] = s[i]
                dic2[t[i]] = s[i]
        # 返回 True
        return True

'''
# @lc code=end

