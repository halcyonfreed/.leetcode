#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        res=0
        while x!=0:
            lastNum=x%10
            if x<0 and lastNum>0:
                lastNum-=10
            
            if res>214748364 or (res==214748364 and (lastNum==8 or lastNum==9)):
                return 0
            if res<-214748364 or (res==-214748364 and lastNum==-9):
                return 0
            
            res=res*10+lastNum
            x=(x-lastNum)//10
        return res

'''
class Solution:
    def reverse(self, x: int) -> int:
        # 记录反转成功之后的结果
        res = 0

        # 对于需要反转的数字 x
        # 每一次都按照【从后向前】的顺序去访问每个元素
        # 在访问过程中会执行一些逻辑判断
        # 判断过程中可能会由于越界直接返回 0 
        # 否则会一直判断下去，直到 x 的每个元素均被访问，即 x = 0 时跳出循环
        while x != 0 :

            # 每一次都先获取末尾数字
            lastNum = x % 10

            # Python3 的取模运算在 x 为负数时也会返回 [0, 9) 以内的结果，因此这里需要进行特殊判断
            if x < 0 and lastNum > 0:
               lastNum -= 10

            # 假设有 1147483649 这个数字，它是小于最大的 32 位整数 2147483647 的
            # 但是将这个数字反转过来后就变成了 9463847411 ，超过了最大的 32 位整数
            # 根据题目要求需要返回 0

            # 在获取到 lastNum 的过程中，需要判断一下当前的 res 是否合法
            # 如果不合法，就不用再添加 lastNum，结果直接返回 0 就行

            # 1、res 为正数并且大于了 214748364 ，即最小为 214748365 ，那么无论 lastNum 为多少，添加上去都会不合法
            # 比如 lastNum 最小为 0 ，形成了 2147483650 ，也是大于 2147483647
            # 2、res 等于了 214748364 ，那么在它的后面添加 8、9，就会形成 2147483648 、2147483649 这两个数
            # 而这两个数都不合法，返回 0
            if res > 214748364 or ( res == 214748364 and (lastNum == 8 or lastNum == 9 )) :
                # 返回 0
                return 0

            
            # 3、res 为负数并且小于了 -214748364 ，即最大为 214748365 ，那么无论 lastNum 为多少，添加上去都会不合法
            # 比如 lastNum 最小为 9 ，形成了 -2147483650 ，也是小于 -2147483648
            # 4、res 等于了 -214748364 ，那么在它的后面添加 9，就会形成 -2147483649 这个数
            # 而这个数不合法，返回 0
            if res < -214748364 or (res == -214748364 and lastNum == -9 ) : 
                # 返回 0
                return 0

        

            # 5、否则说明可以继续添加
            # res 全部元素向左移动，即 10
            res = res  10 + lastNum

            # 6、在去获取 x 的下一个数
            # Python3 的整数除法在 x 为负数时会向下（更小的负数）取整，因此不能写成 x //= 10
            x = (x - lastNum) // 10

        # 返回结果
        return res
'''

# @lc code=end

