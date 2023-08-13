#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 所谓greedy就是和上一步比
        allocate=[1 for _ in range(len(ratings))]

        # 当前比左边大
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                allocate[i]=allocate[i-1]+1

        # 当前比右边大
        result=allocate[-1]
        for i in range(len(ratings)-2,-1,-1):
            # 从倒二，到第一个
            if ratings[i]>ratings[i+1]:
                allocate[i]=max(allocate[i+1]+1,allocate[i])
            
            result+=allocate[i]
        return result


'''
class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 存储每个孩子的糖果        
        # 先给所有孩子 1 颗糖
        candys = [1 for _ in range(len(ratings))]

        # 从左至右遍历数组 ratings
        for i in range( 1 , len(ratings)) :

            # 如果发现当前孩子的评分比【左边】的更高
            if ratings[i] > ratings[i - 1] : 

                # 那么当前孩子的糖果数量需要比【左边】孩子的糖果数量多 1 个
                candys[i] = candys[i - 1] + 1

        
        # 记录糖果数量，初始为最右边的值
        result = candys[-1]

        # 从右至左遍历数组 ratings
        for i in range( len(ratings) - 2 , -1 , - 1 ) :

            # 如果发现当前孩子的评分比【右边】的更高
            if ratings[i] > ratings[i + 1] : 
                
                # 那么当前孩子的糖果数量需要比【右边】孩子的糖果数量多 1 个
                # 当前孩子在第一轮循环中已经设置了值
                # 所以取这两个值的最大值
                # 这样同时满足左规则和右规则 
                candys[i] = max( candys[i + 1] + 1  , candys[i]) 

            

            # candys[i] 已经是符合左规则和右规则的值了
            # 累加到 result 上面
            result += candys[i]
        

        # 返回结果
        return result
'''
# @lc code=end

