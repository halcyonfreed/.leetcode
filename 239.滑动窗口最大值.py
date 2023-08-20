#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # n=len(nums)
        # q=collections.deque()
        # res=[]
        
        # if k<1:
        #     return res
        
        # for i in range(k):
        #     while q and q[-1]<nums[i]:
        #         q.pop()
        #     q.append(nums[i])
        # res.append(q[0])

        # for i in range(k,n):
        #     if q[0]==nums[i-k]:
        #         q.popleft()
            
        #     while q and q[-1]<nums[i]:
        #         q.pop()
        #     q.append(nums[i])
        #     res.append(q[0])
        # return res

        
'''
法医：
登录 AlgoMooc 官网获取更多算法图解
# https://www.algomooc.com
# 作者：程序员吴师兄
# 代码有看不懂的地方一定要私聊咨询吴师兄呀
# 滑动窗口最大值（ LeetCode 239 ）：https://leetcode-cn.com/problems/sliding-window-maximum/
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 获取数组长度
        n = len(nums)
        # 构建双端队列
        q = collections.deque()
        # 建存储最大值的数组
        res = []

        # 边界情况
        if k < 1:
            return res
        # 一开始滑动窗口不包含 K 个元素，不是合格的滑动窗口
        for i in range (k):
            # 在滑动过程中，维护好 deque，确保它是单调递减队列

            # 反复判断，如果队列不为空且当前考察元素大于等于队尾元素，则将队尾元素移除。
            # 直到考察元素可以放入到队列中
            while q and q[-1] < nums[i]:
                q.pop()
            # 考察元素可以放入到队列中
            q.append(nums[i])

        # 这个时候，滑动窗口刚刚好有 k 个元素，是合格的滑动窗口，那么最大值就是队列中的队首元素
        res.append(q[0])

        # 现在让滑动窗口滑动
        for i in range (k, n):
            # 滑动窗口已经装满了元素，向右移动会把窗口最左边的元素抛弃
            # i - k 为滑动窗口的最左边
            # 如果队列的队首元素和窗口最左边的元素相等，需要将队首元素抛出
            # 如果不写这个判断，会导致队列中会包含非当前窗口的元素
            # 比如窗口大小为 1，队列为 1 -1，此时窗口为 【 1 】,队列为 1，输出最大值 1，下一个窗口为 【 -1 】，准备移动的时候队列 1 和数组最左端元素一样，必须移除，否则队列中是 【 1，-1 】，输出的结果是 1，而 1 不在窗口 【 -1 】中
            # while q and nums[q[-1]] <= nums[i]:
            #     q.pop()
            if q[0] == nums[i-k]:
                q.popleft()

            # 反复判断，如果队列不为空且当前考察元素大于等于队尾元素，则将队尾元素移除。
            # 直到考察元素可以放入到队列中
            while q and q[-1] < nums[i]: 
                q.pop()

            q.append(nums[i])

            # 考察元素可以放入到队列中
            res.append(q[0])
        # 最后返回 res
        return res

法二：
登录 AlgoMooc 官网获取更多算法图解
# https://www.algomooc.com
# 作者：程序员吴师兄
# 代码有看不懂的地方一定要私聊咨询吴师兄呀
# 滑动窗口最大值（ LeetCode 239 ）：https://leetcode-cn.com/problems/sliding-window-maximum/
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 获取数组长度
        n = len(nums)
        # 构建双端队列，存储的是 nums 数组中元素的下标
        q = collections.deque()
        # 建存储最大值的数组
        res = []

        # 边界情况
        if k < 1:
            return res
        # 一开始滑动窗口不包含 K 个元素，不是合格的滑动窗口
        for i in range (k):
            # 在滑动过程中，维护好 deque，确保它是单调递减队列

            # 反复判断，如果队列不为空且当前考察元素大于等于队尾元素，则将队尾元素移除。
            # 直到考察元素可以放入到队列中
            # q[-1] 表示队尾元素下标，nums[q[-1]] 则是获取这个下标的元素
            while q and nums[i] >= nums[q[-1]]  :
                q.pop()

            # 考察元素的下标可以放入到队列中
            q.append(i)

        # 这个时候，滑动窗口刚刚好有 k 个元素，是合格的滑动窗口，那么最大值就是队列中的队首元素
        # q[-1] 表示队首元素下标，nums[q[0]] 则是获取这个下标的元素
        res.append(nums[q[0]])

        # 现在让滑动窗口滑动
        for i in range (k, n):
            # 滑动窗口已经装满了元素，向右移动会把窗口最左边的元素抛弃
            # i - k 为滑动窗口的最左边
            # 如果队列的队首元素和窗口最左边的元素相等，需要将队首元素抛出
            # 如果不写这个判断，会导致队列中会包含非当前窗口的元素
            # 比如窗口大小为 1，队列为 1 -1，此时窗口为 【 1 】,队列为 1，输出最大值 1，下一个窗口为 【 -1 】，准备移动的时候队列 1 和数组最左端元素一样，必须移除，否则队列中是 【 1，-1 】，输出的结果是 1，而 1 不在窗口 【 -1 】中
            # q 存储的是下标
            while q and q[0] <= i-k: 
                q.popleft()

            # 反复判断，如果队列不为空且当前考察元素大于等于队尾元素，则将队尾元素移除。
            # 直到考察元素可以放入到队列中
            while q and nums[q[-1]] <= nums[i]:
                q.pop()

            q.append(i)

            # 考察元素可以放入到队列中
            res.append(nums[q[0]])
        # 最后返回 res
        return res
'''
# @lc code=end

