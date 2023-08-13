#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)

        remainGas=0

        for i in range(n):
            remainGas+=gas[i]-cost[i]

        if remainGas<0:
            return -1
        
        currentGas=0
        i=0
        index=0

        while i<n:
            currentGas+=gas[i]-cost[i]

            if currentGas>=0:
                i+=1
            else:
                currentGas=0
                index=i+1
                i+=1
        return index


'''
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 获取加油站的数量
        n = len(gas)

        # 一开始，默认汽车储备的汽油数量为 0
        remainGas = 0

        # 需要统计一下，所有加油站的汽油总量能否支持汽车跑完所有的路程
        for i in range(n) : 
            remainGas += gas[i] - cost[i]
        

        # 如果发现加油站的汽油总量小于所有的路程需要消耗的汽油总量
        # 即汽车最终油箱汽油为负，那无论选择在哪出发，都不可能绕环路行驶一周
        if remainGas < 0 :

            return -1

        # 如果发现加油站的汽油总量大于或者等于所有的路程需要消耗的汽油总量
        # 那么可以绕环路行驶一周，接下来去寻找出发位置

        # 一开始，默认汽车此时储备的汽油数量为 0
        currentGas = 0

        # 一开始，默认汽车出发位置在索引为 0 的加油站
        i = 0

        # index 表示最终选择的出发点，默认为 0
        index = 0

        # 依次遍历每个加油站，在遍历的过程中，会执行一些【跳跃操作】
        while i < n :

            # 汽车在 i 号加油站加了 gas[i]
            # 开到 i + 1 号加油站消耗了 cost[i] 的汽油
            currentGas += gas[i] - cost[i]
            
            # 如果发现油箱里面的汽油是非负数
            # 即汽车可以开到  j 号加油站，j >= i + 1，那么就让汽车继续尝试往前开
            # 寻找出从 i 号加油站出发到最远的加油站的位置 j ，在这期间汽车是会从中间的加油站加油的
            if currentGas >= 0:

                i+=1

            # 如果发现油箱里面的汽油是负数
            # 意味着汽车无法从 i 号加油站开到 j 号加油站，同时也意味着无法从 i + 1 号加油站开到 j 号加油站
            # 那么就直接尝试让汽车从 j 号加油站开始重新出发 
            else:
                
                # 重新初始化汽车油箱油量
                currentGas = 0

                # 最终选择的出发点为 j 号加油站
                index = i + 1

                # 开始出发
                i+=1


        # 最终找到了合适的出发点
        return index
'''
# @lc code=end

