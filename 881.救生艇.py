#
# @lc app=leetcode.cn id=881 lang=python3
#
# [881] 救生艇
#

# @lc code=start
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # dfs: depth-first-search
        people.sort()
        n=len(people)
        left,right= 0, n-1 # 一小配一大来看
        ans=0

        while left<=right:
            if people[left]+people[right]<=limit:
                ans+=1
                left+=1
                right-=1

            else:
                ans+=1
                right-=1
                # 移左边没用
        return ans



'''
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        # 先排序
        people.sort()

        # 获取数组长度
        n = len(people)

        # 寻找两人组

        # 最左边的位置
        left = 0

        # 最右边的位置
        right = n - 1

        # 船的数量
        ans = 0

        while left <= right :
            
            # 1、如果 people[left] + people[right] <= limit
            # 说明 people[left] 和 people[right] 可以同船
           
            if people[left] + people[right] <= limit :

                #  此时船的数量加一
                ans += 1

                # 两个指针分别往中间靠拢

                left += 1

                right -= 1

                
            # 如果 people[left] + people[right] > limit
            # 说明 people[left] 和 people[right] 不可以同船
            else:

                # 由于题目说明了人的重量不会超过 limit
                # people[right] 需要独自坐船，船的数量加一
                ans += 1

                # people[right] 坐船后
                # right 需要向内移动，寻找新的组合
                right -= 1

        # 返回结果
        return ans
'''
# @lc code=end

