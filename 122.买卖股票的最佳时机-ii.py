#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0

        for i in range(1,len(prices)):
            tmp=prices[i]-prices[i-1]
            if tmp>0:
                profit+=tmp
                # 就是贪心，只看相邻的利润差
        return profit

'''

# 登录 AlgoMooc 官网获取更多算法图解
# https://www.algomooc.com
# 作者：程序员吴师兄
# 添加微信 278166530 获取最新课程
# 代码有看不懂的地方一定要私聊咨询吴师兄呀
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 最大利润初始为 0 
        profit = 0

        # 从第 2 天开始（索引为 1 ）
        # 去查看当天是否需要采取【卖出】的操作
        for i in range( 1 , len(prices)) : 

            # 计算当天的股票价格与昨天的股票价格的差值
            tmp = prices[i] - prices[i - 1]

            # 如果发现当天的股票价格大于了昨天的股票价格
            # 那么在当天采取【卖出】操作可以带来正向收益，即产生利润
            # 于是完全可以卖出
            # 而这个利润就可以进行累加起来
            if tmp > 0 : profit += tmp

            # 如果发现当天的股票价格小于了昨天的股票价格
            # 那么不能采取【卖出】操作，因为这会带来负向收益，即产生亏损
            # 导致总的利润值变小
        

        # 返回结果
        return profit
'''
# @lc code=end

