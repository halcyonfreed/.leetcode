#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # 要先排序 不同点

        sets,subset=[],[]
        self.backtrack(0,nums,subset,sets)
        return sets
        
    def backtrack(self, i:int, nums,subset:List[int],sets:List[List[int]]):
        sets.append(subset[:]) # 这里为什么一定要加[:]不加会有问题
        # sets.append(subset)
        # print(subset)
        print(sets,'\n')
        
        
        
        if i>=len(nums):
            return 
        
        for j in range(i,len(nums)):
            # j==i第一个不用剪
            if j>i and nums[j]==nums[j-1]:
                # 剪枝
                continue
            subset.append(nums[j])
            self.backtrack(j+1,nums,subset,sets) # 剩下的可以组成子集吗
            subset.pop() # 如果不要最后一个元素可以有其他选择吗！！！


'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        :param nums: List[int]
        :return: List[List[int]]
        """
        # 先排序，这样才能对比当前元素和之前元素是否相同
        nums.sort()
        
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

            # 4、判断是否需要剪枝，去判断此时存储的数据是否之前已经被存储过
            if j > i and nums[j] == nums[j - 1]:
                continue

            # 把本次递归访问的元素加入到 subset 数组中
            subset.append(nums[j])

            # 4、判断是否需要剪枝，去判断此时存储的数据是否之前已经被存储过
            

            # 5、做出选择，递归调用该函数，进入下一层继续搜索
            # 递归
            self.backtrack(j + 1, nums, subset, sets)

            # 6、撤销选择，回到上一层的状态
            # 取消对 nums[i] 的选择
            subset.pop()
'''
# @lc code=end

