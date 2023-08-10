#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        end=intervals[0][1] # 起始位置
        count=0

        for i in range(1,len(intervals)):
            if intervals[i][0]<end:
                # 发生了重叠
                end=min(end,intervals[i][1]) #删掉尾部长的那个
                count+=1
            else:
                end=intervals[i][1]
        return count
'''
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])  # 左端排序

        end = intervals[0][1]  # 末端位置
        count = 0  # 需要移除的数量

        for i in range(1, len(intervals)):
            if intervals[i][0] < end:  # 发生重叠
                end = min(end, intervals[i][1])  # 更新末端位置
                count += 1  # 移除了一个
            else:  # 没有重叠
                end = intervals[i][1]  # 更新末端位置

        return count

'''
# @lc code=end

