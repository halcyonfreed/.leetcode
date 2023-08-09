#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        factors=[2,3,5]
        seen={1}
        pq=[1]

        for i in range(n-1):
            curr=heapq.heappop(pq)
            for factor in factors:
                if(nxt:=cur*factor) not in seen:
                    seen.add(nxt)
                    heapq.heappush(pq,nxt)
        # 返回结果
        return heapq.heappop(pq)
'''
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 对任意一个丑数来说，去和 2、3、5 分别相乘，可以得到 3 个丑数
        # 那么对每一个丑数都去和 2 、3 、5 分别相乘，把那些结果进行排序即可
        # 因此，2、3、5 就是我们需要处理的质因数
        factors = [2, 3, 5]

        # 由于一些丑数和 2 、 3 、5 相乘会出现重复元素的情况
        # 比如丑数 2 和 2 、 3 、5 相乘得到了 4、【6】、10
        # 而丑数 3 和 2 、 3 、5 相乘得到了 【6】、9 、 15
        # 其中 【6】重复了，所以需要采取去重操作
        # 由于题目说明 n 最大为 1690，会导致丑数的范围超过了 int 范围，所以使用 long 来保存
        

        # 使用优先队列来获取每次集合中最小的数字
        # 由于题目说明 n 最大为 1690，会导致丑数的范围超过了 int 范围，所以使用 long 来保存

        
        # 集合中第一个数字是 1
        # 常量后面跟这种一般是指类型
        # 1L 表示 1 是长整型，如果是 1f 表示是 float 型
        seen = {1}
   

        # 优先队列里面的元素来源于 seen
        pq = [1]

        # 开始不断的迭代丑数的值，直到迭代了 n 次为止
        # 第一个丑数是 1
      

        # 开始迭代
        for i in range(n - 1):

            # 下一个丑数来源于优先队列的队头元素
            curr = heapq.heappop(pq)


            # 本题需要返回 int 型，所以强转一下
            for factor in factors:
                if (nxt := curr * factor) not in seen:
                    seen.add(nxt)
                    heapq.heappush(pq, nxt)


        # 返回结果
        return heapq.heappop(pq)
'''
# @lc code=end

