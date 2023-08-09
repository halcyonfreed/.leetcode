#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt=[0]*26

        for ch in magazine:
            idx=ord(ch)-ord('a')
            cnt[idx]+=1

        for ch in ransomNote:
            idx=ord(ch)-ord('a')
            cnt[idx]-=1

            if cnt[idx]<0:
                return False
        return True
# @lc code=end

