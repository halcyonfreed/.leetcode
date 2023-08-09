#
# @lc app=leetcode.cn id=319 lang=python3
#
# [319] 灯泡开关
#

# @lc code=start
class Solution:
    def bulbSwitch(self, n: int) -> int:
        # return int(sqrt(n))
        return int(sqrt(n+0.5))

'''
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(sqrt(n + 0.5))
'''
# @lc code=end

