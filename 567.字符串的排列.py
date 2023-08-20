#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        res=[]
        p_freq=[0]*26
        for ch in s1:
            idx=ord(ch)-ord('a')
            p_freq[idx]+=1
        
        window=[0]*26

        start=0
        for end in range(len(s2)):
            cur=s2[end]
            idx_cur=ord(cur)-ord('a')
            window[idx_cur]+=1
            if window==p_freq:
                return True
            
            if end>=len(s1)-1:
                chr=s2[start]
                idx_chr=ord(chr)-ord('a')
                window[idx_chr]-=1
                start+=1
        return False



'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 滑动窗口模板化解题，五步走策略

        # 【1、定义需要维护的变量】

        # 题目要求返回这些子串的起始索引，因此使用数组来保存结果，存储的是整型
        res = []

        # 由于都是小写字母，因此直接用 26 个长度的数组代替原来的 HashMap ，比直接使用 HashMap 更优秀
        # needs 代表 p 中每个字符出现的频次
        needs = [0] * 26
        
        # 开始统计 t 中每个字符出现的频次
        for ch in s1:  
            # 对于数组类型，其下标为 int 类型
            # 可以直接使用 char 类型变量，默认强制转换，存储的就是字母对应的 ASCII 码
            # 比如 ch 是 b 字符，那么 b - a = 1，即 needs[1] 表示记录 b 出现的频次 
            idx = ord(ch) - ord('a')
            needs[idx] += 1

        # window 代表在滑动窗口中每个字符出现的频次
        window = [0] * 26

        # 【2、定义窗口的首尾端 (start, end)， 然后滑动窗口】

        # 窗口的左端位置从 0 开始
        start = 0

         # 窗口的右端位置从 0 开始，可以一直移动到尾部
        for end in range(len(s2)):

            # 【3、更新需要维护的变量, 有的变量需要一个 if 语句来维护 (比如最大最小长度)】

            # 获取此时将要加入到滑动窗口的元素
            cur = s2[end]

            # 这个字符的频次需要发生变化
            window[ord(cur) - ord('a')] += 1

            # 加入之后，去对比一下 window 中 cur 这个字符是否满足要求
            if window == needs:
                
                # 相同情况下，找到一个符合条件的索引
                return True
            


            # 【4、如果题目的窗口长度固定：用一个 if 语句判断一下当前窗口长度是否达到了限定长度 】

            # 4.1、如果达到了，窗口左指针前移一个单位，从而保证下一次右指针右移时，窗口长度保持不变,
            if  end >= len(s1) - 1 :
                
                # 4.2、更新 (部分或所有) 维护变量 
                chr = s2[start]

                # 最左端那个元素的频次发生变化
                window[ord(chr) - ord('a')] -= 1

                # 4.3、窗口左指针前移一个单位保证下一次右指针右移时窗口长度保持不变
                start += 1
 

        # 【5、返回所需要的答案】
        return False
'''
# @lc code=end

