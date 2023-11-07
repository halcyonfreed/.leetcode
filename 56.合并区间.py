#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0]) # 用x[0]排序
        result=[]

        for i in range(len(intervals)):
            left=intervals[i][0]
            right=intervals[i][1]

            if not result:
                result.append(intervals[i])
                continue
            
            last=result[-1]
            if last[1]<left:
                result.append(intervals[i])
            else:
                newRight=max(last[1],right)
                result[-1][1]=newRight
        return result
# @lc code=end

