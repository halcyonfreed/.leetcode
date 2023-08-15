#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=='0' or num2=='0':
            return "0"
        m,n=len(num1),len(num2)
        ansArr=[0]*(m+n)

        for i in range(m-1,-1,-1):
            x=int(num1[i])
            for j in range(n-1,-1,-1):
                y=int(num2[j])
                ansArr[i+j+1]+=x*y
        
        for k in range(m+n-1,0,-1):
            ansArr[k-1]+=ansArr[k]//10
            ansArr[k]%=10

        
        index=1 if ansArr[0]==0 else 0

        ans="".join(str(x) for x in ansArr[index:])
        return ans

'''
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # 边界处理，任何数和 0 相乘都为 0 
        if num1 == "0" or num2 == "0":
            # 直接返回 0
            return "0"

        # 获取字符串 num1 的长度
        m = len(num1) 
        
        # 获取字符串 num2 的长度
        n = len(num2)

        # 基于这两个长度可以构造一个长度为 m + n 的数组
        # 因为假设 m = 2 ，最大数是 99
        # n = 3 ，最大数是 999
        # 两者相乘的结果 98901 长度为 5 
        ansArr = [0] * (m + n)

        # 从后向前依次访问 num1 中的元素
        for i in range(m - 1, -1, -1):

            # '0' 的 ASCII 码是 48 ，'1' 的是 49 
            # 获取数字，相当于字符串转整数操作
            x = int(num1[i])

            # 从后向前依次访问 num2 中的元素
            for j in range(n - 1, -1, -1):
                
                # '0' 的 ASCII 码是 48 ，'1' 的是 49 
                # 获取数字，相当于字符串转整数操作
                y = int(num2[j])

                # 把 x 和 y 相乘的结果存放到 i + j + 1 位
                # 比如一开始 i = m - 1 、j = n - 1 
                # 那么就存放到 m - 1 + n - 1 + 1 = m + n - 1
                # 数组的索引是从 0 开始 ，即此时存放到了最后一位
                # 并且由于 x 和 y 必然都是个位数，相乘的结果最多只能是两位数
                ansArr[ i + j + 1 ] += x * y



        # 接下来，需要把 ansArr 的每一位都拿出来查看一下
        # 使得每一个都只存放一位数字，多余的传递给上一层
        for k in range(m + n - 1, 0, -1):

            # 上一位的数字需要累加当前这一位的十位数
            # 比如 ansArr[k] = 24 ， ansArr[k - 1]  = 68
            # 那么 ansArr[k - 1] 需要加上 2 ，变成了 70
            ansArr[k - 1] += ansArr[k] // 10

            # 然后 ansArr[k] 就更新为它的个位数
            ansArr[k] %= 10

        # 最后，开始把数组转换为字符串的形式
        

        # 从最高位开始接收
        # 此时，需要判断一下 ansArr[0] 是否为 0 ， 如果为 0 ，那么就抛弃这一位，从下一位在开始接收
        index = 1 if ansArr[0] == 0 else 0

        # 不断的去填充字符串
        ans = "".join(str(x) for x in ansArr[index:])

        # 最后返回结果
        return ans
'''
# @lc code=end

