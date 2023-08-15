#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        n=len(s)
        index=0
        res=0
        # 完全类似7

        negative=False
        while index<n and s[index]==" ":
            index+=1
        if index==n:
            return 0
        
        if s[index]=="-":
            negative=True

        if s[index]=='-' or s[index]=='+':
            index+=1
        

        # while index<n and '9'>=s[index]>='0':
        while index<n and '9'>=s[index] and s[index]>='0':
            lastNum=ord(s[index])-48

            if not negative and (res>214748364 or (res==214748364 and (lastNum==8 or lastNum==9))):
                return 2147483647
            
            if negative and (res<-214748364 or (res==-214748364 and  (lastNum==8 or lastNum==9))):
                return -2147483648
            
            res=res*10+lastNum
            index+=1
        return -res if negative else res
    # 测试用例有问题 tmd的
'''
class Solution:
    def myAtoi(self, s: str) -> int:
        # 字符串的长度
        n = len(s)

        # 设置有效数字的索引位置，初始化在第 0 个
        index = 0

        # 接收最终的结果
        res = 0

        # 根据第二点要求：检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。 确定最终结果是负数还是正数。
        # 所以在扫描的过程中，需要不断的判断最终的结果是正数还是负数
        # 根据字符的正和负来判断，最后一个字符决定
        # 默认为正数，即不是负数
        negative = False

        # 根据第一点要求：读入字符串并丢弃无用的前导空格
        while index < n and s[index] == ' ' :

            # 有效数字的索引位置不断移动
            index += 1

        

        # 根据第四点要求：如果字符串全是空格直接返回 0
        if index == n :
            
            # 直接返回 0
            return 0

        # 根据第二点要求：检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。 确定最终结果是负数还是正数。
        # 如果发现是负数，修改判断
        if s[index] == '-' :

            # 认为是负数
            negative = True

        

        # 跳过正负号符号位
        if s[index] == '-' or s[index] == '+' :

            # 有效数字的索引位置不断移动
            index += 1

        

        # 开始获取数字，一个数字一个数字去获取
        # 由于在字符串中可能存在数字之间夹杂的其它字符，所以出现这种情况需要截断
        while index < n and s[index] >= '0'and s[index] <= '9' :

            # '0'的 ASCII 码是48，'1' 的是 49 
            # 获取数字，相当于字符串转整数操作
            lastNum =  ord(s[index]) - 48
            

            # 根据第五点要求：需要判断数字是否合理
            # 先判断正数情况，大于 2147483647 的整数应该被固定为 2147483647 
            # 即如何发现之前积累的数字都大于了 214748364，比如最小为 214748365
            # 那么无论 lastNum 为多少，添加到尾部都会大于 214748364
            if not negative and ( res > 214748364 or ( res == 214748364 and (lastNum == 8 or lastNum == 9 ))) :

                # 应该被固定为 2147483647 
                return 2147483647

        

            # 根据第五点要求：需要判断数字是否合理
            # 再判断负数情况，小于 -2147483648 的整数应该被固定为 -2147483648 
            if negative and ( -res < -214748364 or ( -res == -214748364 and (lastNum == 8 or lastNum == 9 ) )) :
                # 应该被固定为 -2147483648 
                return -2147483648
            

            # 否则说明可以添加上去
            res = res * 10 + lastNum

            # 有效数字的索引位置不断移动
            index += 1


        # 返回整数作为最终结果。
        return -res if negative else res
'''
# @lc code=end

