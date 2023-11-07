#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 耐心看完了讲解
        sets,subset=[],[]
        self.backtrack(0,nums,subset,sets)
        return sets

    def backtrack(self,i:int,nums:List[int],subset:List[int],sets:[List[List[int]]]):
        sets.append(subset[:]) # 加上去
        if i>=len(nums):
            return 
        
        for j in range(i,len(nums)):
            # 类似排列组合的全排列
            subset.append(nums[j])
            self.backtrack(j+1,nums,subset,sets) # 套娃，对从j+1开始的继续
            subset.pop()



'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        :param nums: List[int]
        :return: List[List[int]]
        """
        # 结果集合
        sets = []

        # 每次的子集
        subset = []

        # 执行回溯算法
        self.backtrack(0, nums, subset, sets)

        # 返回结果
        return sets

    def backtrack(self, i, nums, subset, sets):
        """
        :param i: int
        :param nums: List[int]
        :param subset: List[int]
        :param sets: List[List[int]]
        """
        # 每次确定好一个子集，都把它加入到结果集合中
        sets.append(subset[:])

        # 2、寻找结束条件，由于回溯算法是借助递归实现，所以也就是去寻找递归终止条件
        # 本题中可以不加这个判断，大家可以思考一下为什么可以不加，结合 for 循环的边界来思考
        if i >= len(nums):
            return

        for j in range(i, len(nums)):
            # 把本次递归访问的元素加入到 subset 数组中
            subset.append(nums[j])

            # 4、判断是否需要剪枝，去判断此时存储的数据是否之前已经被存储过
            # 本题不需要剪枝

            # 5、做出选择，递归调用该函数，进入下一层继续搜索
            # 递归
            self.backtrack(j + 1, nums, subset, sets)

            # 6、撤销选择，回到上一层的状态
            # 取消对 nums[i] 的选择
            subset.pop()
'''
# @lc code=end

