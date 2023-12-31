#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt=[0]*32 # 根据提示来的，空间换时间
        for i in range(len(nums)):
            num=nums[i]
            for j in range(32):
                temp=num>>j
                x=temp&1 
                if x==1:
                    cnt[j]+=1
        
        ans=0
        for i in range(32):
            temp=cnt[i]%3
            if temp==1:
                num=1<<i
                ans+=num
        return ans if cnt[31]%3==0 else ~(ans ^ 0xffffffff)




'''
#登录 AlgoMooc 官网获取更多算法图解
# https://www.algomooc.com
# 作者：程序员吴师兄
# 代码有看不懂的地方一定要私聊咨询吴师兄呀
# 只出现一次的数字 II（ LeetCode 137 ）:https://leetcode-cn.com/problems/single-number-ii
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # 设置一个长度为 32 位的数组
        # 在这个数组中，每一位存储的就是 nums 数组中每一位二进制形式相加后 1 的个数
        cnt = [0] * 32

        # 遍历 nums 数组
        # 虽然这里有两个 for 循环，但是内层循环的 n 是常数，因此时间复杂度依旧为 O n)
        for  i in range(len(nums)) : 
            
            # 获取第 i 位的数字
            num = nums[i]

            # 将 num 展开为二进制的形式，有 32 位
            for j in range(32) : 

               
                # >> 表示右移符号，右移运算是将一个二进制位的操作数按指定移动的位数向右移动，移出位被丢弃
                # >> j 表示右移了 j 位
                # 比如 nu=2 的二进制表示为 
                # 0000 0000 0000 0000 0000 0000 0000 0010
                # >> 1 之后变成了 相当于/2
                # 000 0000 0000 0000 0000 0000 0000 0001
                #  在计算机中默认为 0 ，所以结果就是 0000 0000 0000 0000 0000 0000 0000 0001
                temp = num >> j


                # & 表示按位与运算符，只有对应的两个二进位都为 1 时，结果位才为 1
                # 每次将 num 向右移动之后，都将移动后的数和 1 进行按位与操作
                # 这样就得到了 num 中第 i 个二进制位
                # 比如 num 的二进制表示为 
                # 0000 0000 0000 0000 0000 0000 0000 0010
                # 当 j = 0 时，temp 为 【】代表最后一位
                # 0000 0000 0000 0000 0000 0000 0000 001【0】 # temp 的二进制表示
                # &
                # 0000 0000 0000 0000 0000 0000 0000 000【1】 # 1 的二进制表示
                # =
                # 0000 0000 0000 0000 0000 0000 0000 000【0】 # 等于 0
                # 即 num 的第 0 个位置的二进制位 0
                # < -------------->
                # 当 j = 1 时，temp 为
                # 0000 0000 0000 0000 0000 0000 0000 000【1】 # temp 的二进制表示
                # &
                # 0000 0000 0000 0000 0000 0000 0000 000【1】 # 1 的二进制表示
                # =
                # 0000 0000 0000 0000 0000 0000 0000 000【1】 # 等于 1
                # 即 num 的第 1 个位置的二进制位 1
                x = temp & 1

                # 如果第 j 位的二进制位是 1，把它累加到 cnt[j] 上
                # cnt[j] 表示 nums 数组中每一个数字二进制形式表示后，第 j 位有多少个 1
                if   x == 1 :
                    cnt[j] += 1
                
            

        

        # 使用 ans 用来记录 nums 中那个只出现了一次的元素
        # 一开始 ans 的二进制表示为 
        # 0000 0000 0000 0000 0000 0000 0000 0000 
        # 即由 32 个 0 组成
        ans = 0
        
        # 此时，cnt 已经存储的 nums 数组中每一位二进制形式相加后 1 的个数
        # 遍历每个位置
        for  i in range(32) :
            
            # 因为相同数字的二进制表示是一样的，也就意味着如果它出现了三次，那么这个数字相加三次之后，
            # 在某个位置上出现 1 的次数要么是 0 次，要么是 3 次
            # 比如数字 2，它的二进制是  0000 0000 0000 0000 0000 0000 0000 00【1】0
            # 出现三次时，【1】 也必然出现三次
            # 将某个位置相加的结果除以 3，如果余数为 1，表明只出现了一次
            temp = cnt[i] % 3

            # 把出现了一次的二进制位添加到 ans 上
            if  temp == 1 :

                # << 表示左移符号，用来将一个数的各二进制位全部左移若干位
                # 移动的位数由右操作数指定，右操作数必须是非负值，其右边空出的位用 0 填补，高位左移溢出则舍弃该高位
                # 这个操作就是不断的填充二进制
                num = 1 << i

                # 把二进制结果累加到 ans 上
                ans += num
            
        

        # 返回 ans 就行 
        # 在 Python 中需要对最高位进行特殊判断。
        return ans if cnt[31] % 3 == 0 else ~(ans ^ 0xffffffff)
'''
# @lc code=end

