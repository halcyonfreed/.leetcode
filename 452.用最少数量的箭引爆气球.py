#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#

# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda balloon:balloon[1]) # 按末端排序

        pos=points[0][1]
        res=1

        for balloon in points:
            if balloon[0]>pos:
                pos=balloon[1]
                res+=1
        return res


'''
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
    

        # 第一步，先将原数组进行一个排序的操作
        points.sort(key=lambda balloon: balloon[1])

        # 此时，第一只箭的位置在第一个数组的末端，即最右侧位置
        pos = points[0][1]

        # res 代表箭的数量
        res = 1

        # 开始遍历排序好后的那些气球数组
        # 这些气球数组按照末端的大小进行了升序排序
        for balloon in points:

            # 在遍历过程中，只要发现当前气球的左端位置超过了当前箭头的位置
            # 那么代表着此时这只 pos 箭无法引爆 balloon 这个气球
            # 那么需要增加其它的箭
            if  balloon[0] > pos :

                # 新增的箭放在当前气球的最右端
                pos = balloon[1]

                # 同时，更新了箭的数量
                res += 1
  
        return res
'''
# @lc code=end

