#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self,s:str, t:str)->bool:
        if len(s)!=len(t):
            return False
        table=26*[0]
        for i in s :
            index=ord(i)-ord('a')
            table[index]+=1
        for i in t:
            index=ord(i)-ord('a')
            table[index]-=1
            if table[index]<0:
                return False
        return True

# @lc code=end

