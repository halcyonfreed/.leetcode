#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map=dict()
        for i,num in enumerate(nums):
            anotherNum=target-num
            if anotherNum in map:
                return [map[target-num],i]
            else:
                map[nums[i]]=i
        return []

'''
# 登录 AlgoMooc 官网获取更多算法图解
# https://www.algomooc.com
# 作者：程序员吴师兄
# 代码有看不懂的地方一定要私聊咨询吴师兄呀
# 两数之和（LeetCode 1）:https://leetcode-cn.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       # 首先构建一个哈希表，用来存放数组的元素值以及索引值
       # 其中 key 是数组中的元素值
       # value 为数组中元素值的索引
       map = dict()

       # 接下来，遍历整个数组
       for i, num in enumerate(nums):
           # 目标值为 target，将 target 与 nums[i] 求差
           # 获取与 nums[i] 配对的那个数 anotherNum
           anotherNum = target - num

           # 判断哈希表中是否存在那个与 nums[i] 配对的数 anotherNum
           if anotherNum in map :

               # 由于哈希表中所有 key 都是来自于数组中，
               # 所以，如果发现哈希表存在那个与 nums[i] 配对的数 anotherNum
               # 也就说明数组中存在一个数，可以和 nums[i] 相加为 target
               # 此时， anotherNum 这个 key 对应的 value 为这个数在数组中的索引
               # 所以，返回 map.get(anotherNum) 和 i 就是这两个值的下标
               return [ map[ target - num ] , i ]
           else:
              # 如果发现哈希表中目前不存在那个与 nums[i] 配对的数 anotherNum
              # 那么就把此时观察的数 nums[i] 和它的索引存放到哈希表中
              # 等待后面的数能和它配对为 target
             map[nums[i]] = i

       # 如果遍历完整个数组都找不到和为 target 的两个数，返回 0
       return []
'''
# @lc code=end

