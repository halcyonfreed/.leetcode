#
# @lc app=leetcode.cn id=373 lang=python3
#
# [373] 查找和最小的 K 对数字
#

# @lc code=start
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m,n=len(nums1),len(nums2)
        # value, nums1 的索引和 nums2 的索引
        # pq:priority queue 把 nums2 中的第一个元素和 nums1 中的每个元素都先组合一下，存放到优先队列当中
        pq=[(nums1[i]+nums2[0],i,0) for i in range(min(k,m))]
        ans=[]

        while pq and len(ans)<k:
            # https://blog.csdn.net/chandelierds/article/details/91357784
            _,index1,index2=heappop(pq)
            ans.append([nums1[index1],nums2[index2]])

            index2+=1
            if index2<n:
                heappush(pq,(nums1[index1] + nums2[index2],index1, index2))
        return ans

'''
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # PriorityQueue 里面的每个元素是一个数组，这个数组包含了两个元素，表示 nums1 的索引和 nums2 的索引
        # 由于 nums1 和 nums2 都是升序序列，最小的组合就是 nums1[0] + nums2[0]
        # 接下来的组合需要经过比较
        # 和谁比较呢
        # 可以把 nums2 中的第一个元素和 nums1 中的每个元素都先组合一下，存放到优先队列当中

        m, n = len(nums1), len(nums2)
        pq = [(nums1[i] + nums2[0], i, 0) for i in range(min(k, m))]

        # 结果数组
        ans = []

        # 访问优先队列，不断的弹出队头元素，最多弹 k 次就行
        while pq and len(ans) < k:
            
            # 取出队头元素
            # pos 是一个数组，包含两个元素，表示 nums1 的索引和 nums2 的索引
            _,index1, index2 = heappop(pq)
            
            # 利用这两个索引获取到对应的元素进行组合
            ans.append([nums1[index1], nums2[index2]])

            # 获取下一个索引
            index2 += 1

            # 判断 nums2 中是否还有元素
            if index2 < n : 
                # 如果有，那么又是一个新的组合
        
                # 加入到优先队列，在内部会自动进行排序操作
                heappush(pq, (nums1[index1] + nums2[index2],index1, index2))

        # 返回结果
        return ans
'''
# @lc code=end

