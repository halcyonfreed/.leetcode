#
# @lc app=leetcode.cn id=605 lang=python3
#
# [605] 种花问题
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i=0 #指针
        while i<len(flowerbed) and n>0:
            if flowerbed[i]==1:
                i+=2 #显然直接跳过一个
            # elif flowerbed[i+1]==0 or i==len(flowerbed)-1: #交换一下位置都不行 why
            elif i==len(flowerbed)-1 or flowerbed[i+1]==0:
                # 当前是0，下一个是0
                n-=1
                i+=2
            else:
                # 当前是0，下一个是1
                i+=3
        return n<=0 # 而不是==0
'''

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
     # 遍历数组，在遍历过程中，采取贪心的思路，并不需要【每个位置】都去查看是否可以种花
       # 1、当前位置已经种花，那么后一个位置明显不能种花，可以跳过去
       # 2、当前位置没有种花，需要考虑后面一个位置是否种花

       i = 0 

       while i < len(flowerbed) and n > 0 :

           # 1、当前位置已经种花，那么后一个位置明显不能种花，可以跳过去
           # 所以让 i 执行加 2 操作，跳过了加 1 后的那个位置
           if flowerbed[i] == 1 :

               # 让 i 执行加 2 操作
               i += 2

           # 2、说明当前位置没有种花 flowerbed[i] == 0
           # 3、如果这个位置是数组的最后一个位置，说明后一个位置不存在，没有限制，说明 flowerbed[i] 可以种花
           # 4、如果这个位置【不是】数组的最后一个位置，那么只有后一个位置【没有种花】，才有资格在 flowerbed[i] 位置种花
           elif i == len(flowerbed) - 1 or flowerbed[i + 1] == 0 :

               # 以上两种条件都可以在 flowerbed[i] 位置种花
               # 成功之后，所需目标减 1
               n -= 1
               
               # 在 flowerbed[i] 位置种花之后，i + 1 位置不需要去考虑了，因为它明显不能种花，可以跳过去
               # 让 i 执行加 2 操作
               i += 2
            
           # 5、说明当前位置没有种花 flowerbed[i] == 0
           # 6、但是后一个位置已经种花了，那么当前位置无法采取种花操作
           else:

               # i + 1 位置已经种花，不用再去访问一遍
               # i + 2 位置考虑到 i + 1 位置已经种花，所以也无法种花，不用再去访问
               # 让 i 执行加 3 操作
               i += 3

       # 最后查看是否用完了 n
       return n <= 0
'''
# @lc code=end

