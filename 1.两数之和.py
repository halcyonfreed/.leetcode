#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record_hash={}
        # record_hash=dict()

        # hap map
        for index, num in enumerate(nums):
            # 也要存下标index 作为value； num作为key 被查询对象
            other=target-num 
            if other in record_hash:
                # 在dict 查找key
                return [index,record_hash[other]]
            record_hash[num]=index
            # 也下面两行可以这么写
            # else: 
            #     record_hash[num]=index
        return []


'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        records = dict()

        for index, value in enumerate(nums):  
            if target - value in records:   # 遍历当前元素，并在map中寻找是否有匹配的key
                return [records[target- value], index]
            records[value] = index    # 如果没找到匹配对，就把访问过的元素和下标加入到map中
        return []
'''


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

