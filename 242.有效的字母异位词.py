#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self,s:str, t:str)->bool:
        record=[0]*26
        # string 1 遍历
        for i in s:
            record[ord(i)-ord('a')]+=1
        for i in t:
            record[ord(i)-ord('a')]-=1
        
        # 判断
        for i in range(26):
            if record[i]!=0:
                return False
        return True
        # print(record)
        # return not all(record[i] for i in range(26)) # 这种写法不对！！

        # if len(s)!=len(t):
        #     return False
        # table=26*[0]
        # for i in s :
        #     index=ord(i)-ord('a')
        #     table[index]+=1
        # for i in t:
        #     index=ord(i)-ord('a')
        #     table[index]-=1
        #     if table[index]<0:
        #         return False
        # return True
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0] * 26
        for i in s:
            #并不需要记住字符a的ASCII，只要求出一个相对数值就可以了
            record[ord(i) - ord("a")] += 1
        for i in t:
            record[ord(i) - ord("a")] -= 1
        for i in range(26):
            if record[i] != 0:
                #record数组如果有的元素不为零0，说明字符串s和t 一定是谁多了字符或者谁少了字符。
                return False
        return True
'''


# @lc code=end

