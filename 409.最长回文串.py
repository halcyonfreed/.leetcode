#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        ls=list(s)
        cnt={} # hash dict表
        for word in ls:
            cnt[word]=0 # 初始化 不然没法加

        for word in ls:
            cnt[word]+=1

        ans=0
        # 遍历dict要用.items()
        for key,value in cnt.items():
            if value % 2==0:
                ans+=value
            else:
                ans+=value-1
                cnt[key]=1
        return ans+1 if 1 in cnt.values() else ans


'''
class Solution:
    def longestPalindrome(self, s: str) -> int:

        # 手动设置哈希表，哈希函数为 c - 'A'
        # 这里的哈希表的作用是计数器
        # 由于 大写字母 'A' 与小写字母 'a' 的 ASCII 相差 32
        # A : 65
        # a : 97
        # 所以设置哈希表的大小为 32 + 26 = 58
        l_s = list(s)
        #字典来存储每个字母出现的个数
        cnt = {}
        for word in l_s:
            cnt[word] = 0

        for word in l_s:
            cnt[word] += 1

        ans = 0

        for key, value in cnt.items():
            #如果出现个数为偶数，直接加入
            if value % 2 == 0:
                ans += value
            else:
                #如果为奇数，则加value - 1，并且，该字母的次数变为1
                ans += value - 1
                cnt[key] = 1 
       
        return  ans + 1 if 1 in cnt.values() else ans
'''
        
# @lc code=end

