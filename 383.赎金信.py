
#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # cnt=[0]*26

        # for ch in magazine:
        #     idx=ord(ch)-ord('a')
        #     cnt[idx]+=1

        # for ch in ransomNote:
        #     idx=ord(ch)-ord('a')
        #     cnt[idx]-=1

        #     if cnt[idx]<0:
        #         return False
        # return True

        #  ransomNote 能不能由 magazine 里面的字符构成，所以ransomNote是被magazine包含！！

        # # 法一：自己想的，仿照242 找异位词改的
        # cnt=[0]*26

        # for m in magazine:
        #     cnt[ord(m)-ord('a')]+=1
        # for r in ransomNote:
        #     cnt[ord(r)-ord('a')]-=1
        # for i in range(26):
        #     if cnt[i]<0:
        #         return False
        # return True

#  代码随想录 标准答案！
        ransom_count = [0] * 26
        magazine_count = [0] * 26
        for c in ransomNote:
            ransom_count[ord(c) - ord('a')] += 1
        for c in magazine:
            magazine_count[ord(c) - ord('a')] += 1

        # a=[ransom_count[i] <= magazine_count[i] for i in range(26)]
        # return all(a)
        return all(ransom_count[i] <= magazine_count[i] for i in range(26))



'''
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = [0] * 26
        magazine_count = [0] * 26
        for c in ransomNote:
            ransom_count[ord(c) - ord('a')] += 1
        for c in magazine:
            magazine_count[ord(c) - ord('a')] += 1
        return all(ransom_count[i] <= magazine_count[i] for i in range(26))
'''


# @lc code=end

