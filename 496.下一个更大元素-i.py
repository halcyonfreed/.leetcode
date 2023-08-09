#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res,stack={},[]

        for num in reversed(nums2):
            while stack and num>=stack[-1]:
                stack.pop()

            res[num]=stack[-1] if stack else -1
            stack.append(num)

        ans=[]
        for num in nums1:
            ans.append(res[num])
        return ans
    
'''
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # 先计算 nums2 • 中每个元素右边的第一个更大的值
        # 结果存放到一个哈希集合里面
        # key 是 nums2 中的元素
        # value 是这个元素右边的第一个更大的值
        res = {}

        # 设置一个栈
        # 这个栈是一个单调递增栈
        stack = []

        # 从后向前访问 nums 中的元素
        for num in reversed(nums2):

            # 在访问过程中
            # 维护单调递增栈的性质
            # 不断的去拿栈顶元素和当前元素 num 比较
            # 1、直到找到一个比 num 更大的元素为止
            # 2、或者栈为空位置
            while stack and num >= stack[-1]:
                # 出栈操作
                stack.pop()

            # 1、如果栈不为空，那么此时的栈顶元素就是一个比 num 更大的元素
            # 存放栈顶元素值到哈希集合 res 中
            # 2、如果栈为空，说明在 num 的右侧没有任何一个元素比它更大
            # 存放 -1 到哈希集合 res 中
            res[num] = stack[-1] if stack else -1

            # 把当前元素加入到栈中
            stack.append(num)
        
        # 初始结果数组
        ans = []

        # 1、由于两个数组都是没有重复元素的数组
        # 2、nums1 是 nums2 的子集
        for num in nums1 :
            # 那么就去哈希集合 res 中找出对应元素的值来
            ans.append(res[num])

        # 返回结果
        return ans
'''
# @lc code=end

