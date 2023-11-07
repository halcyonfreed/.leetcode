#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sets=[] # 结果[[],[],[]]
        path=[] 
        used=[False]* len(nums)

        self.backtrack(nums,path,used,sets)
        return sets

    def backtrack(self,nums:List[int],path:List[int],used:List[bool], sets: List[List[int]]):
        # path就是树枝，箭头上的元素
        if len(path)==len(nums):
            sets.append(path[:])
            return
        
        for i in range(len(nums)):
            if not used[i]:
                path.append(nums[i])
                used[i]=True
                self.backtrack(nums,path,used,sets)

                # 对nums[i]撤销
                used[i]=False
                path.pop()


'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        :param nums: List[int]
        :return: List[List[int]]
        """
        # 结果集合
        sets = []

        # 每次的子集
        path = []

        used = [False] * len(nums)

        # 执行回溯算法
        self.backtrack(nums, path, used, sets)

        # 返回结果
        return sets

    def backtrack(self, nums, path, used, sets):
        """
        :param nums: List[int]
        :param path: List[int]
        :param used: List[bool]
        :param sets: List[List[int]]
        """
        # 2、寻找结束条件，由于回溯算法是借助递归实现，所以也就是去寻找递归终止条件
        if len(path) == len(nums):
            # 每次确定好一个子集，都把它加入到结果集合中
            sets.append(path[:])
            return

        for i in range(len(nums)):
            if not used[i]:
                # 把本次递归访问的元素加入到 subset 数组中
                path.append(nums[i])

                used[i] = True

                # 4、判断是否需要剪枝，去判断此时存储的数据是否之前已经被存储过
                # 本题不需要剪枝
                # 5、做出选择，递归调用该函数，进入下一层继续搜索
                # 递归
                self.backtrack(nums, path, used, sets)

                # 6、撤销选择，回到上一层的状态
                # 取消对 nums[i] 的选择
                used[i] = False
                path.pop()
'''
# @lc code=end