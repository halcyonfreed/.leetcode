#
# @lc app=leetcode.cn id=1052 lang=python3
#
# [1052] 爱生气的书店老板
#

# @lc code=start
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        unsatisfied=[c*g for c,g in zip(customers,grumpy)] # 每分钟满意的人数
        win_sum=sum(unsatisfied[:minutes])
        max_win_sum=win_sum # 初值

        # 冷静下来能挽回的顾客！！
        for right, num in enumerate(unsatisfied[minutes:],minutes):
            # right的编号从minutes开始
            win_sum+=num
            left=right-minutes
            win_sum-=unsatisfied[left]
            max_win_sum=max(max_win_sum,win_sum)
        return sum(customers)-sum(unsatisfied)+max_win_sum

'''
# 题目：LC1052. 爱生气的书店老板
# 难度：中等
# 算法：固定滑窗

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # 假设书店老板无法控制不生气，那么不满意的客人数目是恒定的，
        # 为sum([customers[i]*grumpy[i] for i in range(n)])，n为书店开张分钟
        # 为了使得总的不满意的客人数目尽可能地小，
        # 书店老板在连续的minutes分钟中抑制不生气，使得不满意客人数目的减少量要尽可能地大
        # 因此把问题转化为了在【长度为minutes的滑动窗口中，使得不满意客人减少量尽可能地大】的滑动窗口问题
        
        unsatisfied = [c * g for c, g in zip(customers, grumpy)]
        win_sum = sum(unsatisfied[:minutes])
        max_win_sum = win_sum

        for right, num in enumerate(unsatisfied[minutes:], minutes):
            # A1
            win_sum += num
            # A2
            left = right - minutes
            win_sum -= unsatisfied[left]
            # A3
            max_win_sum = max(max_win_sum, win_sum)

        # 总人数 - 原本总不满意人数 + 克制住没生气挽回的不满意人数 = 最终满意人数
        return sum(customers) - sum(unsatisfied) + max_win_sum

'''
# @lc code=end

