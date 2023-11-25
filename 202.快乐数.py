#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        record_sum=set()
        while True:
            n=self.get_sum(n)
            # if n ==1:
            #     return True # 如果正好就是1，就直接出来了可以
            # if n in record_sum:
            #     return False
            # else:
            #     record_sum.add(n)

            # 这么写也对！！！
            if n ==1:
                return True # 如果正好就是1，就直接出来了可以
            else:
                if n in record_sum:
                    return False
                else:
                    record_sum.add(n)
    def get_sum(self,n:int)->int:
        new_num=0
        while n:
            n,r=divmod(n,10) #妙啊，同时更新n了！！！
            new_num+=r**2
        return new_num
'''
class Solution:
    def isHappy(self, n: int) -> bool:        
        record = set()

        while True:
            n = self.get_sum(n)
            if n == 1:
                return True
            
            # 如果中间结果重复出现，说明陷入死循环了，该数不是快乐数
            if n in record:
                return False
            else:
                record.add(n)

    def get_sum(self,n: int) -> int: 
        new_num = 0
        while n:
            n, r = divmod(n, 10)
            new_num += r ** 2
        return new_num
'''

# @lc code=end

