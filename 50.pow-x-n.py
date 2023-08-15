#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1.0
        elif n==-1:
            return 1/x
        elif n&1 ==0: 
            # n是偶数
            return self.myPow(x*x,n//2)
        
        else:
            return self.myPow(x*x,n//2)*x
        #     if n>0:
        #         # 奇数
        #         return x*self.myPow(x*x,n//2)
        #     else:
        #         return self.myPow(x*x,n//2)*x

'''
class Solution:
    def myPow(self, x: float, n: int) -> float:


        # 递归终止条件
        if n == 0 :
            return 1.0    
        elif n == -1 :
            # 任何数的 0 次方的结果都是 1 ，由于题目要求返回 double 类型，因此返回 1.0
            return 1/x
        # 判断 n 是奇数还是偶数
        # 1、如果是偶数
        elif n & 1 == 0 :
            # 那么只需要先计算出 y = x * x 的结果
            # 然后 y 的次幂就是 n / 2
            return self.myPow(x * x, n // 2)

        # 2、如果是奇数
        else :

            # 比如 n = 9 ，那么它就可以被划分为 4 + 4 + 1，即 x^4 * x^4 * x
            # 并且，这个时候还需要判断一下 n 是否为负数

            # 如果是正数
            if n > 0  :

                # 直接抽离出一个 x 来，然后和 myPow(x * x, n / 2) 进行相乘
                return x * self.myPow(x * x, n // 2)

            # 如果是负数
            else :
                # 比如 n = -9
                # Python 比较特殊，正数负数除以 2 取整有区别
                # a = -9
                # b = a // 2
                # print(b) 输出为 -5
                # 此时 n / 2 = -5
                # (x * x)^-5 = x ^ -10
                # 因此 myPow(x * x, n / 2) 的结果还差一个 x ^ 1 才能还原原来的结果 x ^ -9
                # 由于题目要求返回 double 类型，因此这里使用 1.0
                return self.myPow(x * x, n // 2) * x
'''
# @lc code=end

