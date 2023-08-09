#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # s="leetcode"
        cnt=Counter(s)
        # print(cnt)

        for i,v in enumerate(s):
            if cnt[v]==1:
                return i
        return -1

'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Counter 可以直接统计字符串、列表等可迭代对象的元素频率
        # s = "leetcode"
        # cnt = Counter({'e': 3, 'l': 1, 't': 1, 'c': 1, 'o': 1, 'd': 1})
        cnt = Counter(s)
        print(cnt)

        # 如果想在for循环中同时获得列表的索引 i 和元素值 v
        # 可以使用枚举内置函数 enumerate()
        for i, v in enumerate(s):
            # 如果找到了某个字符出现的频率为 1
            if cnt[v] == 1:
                # 返回它的下标即可
                return i

        # 如果不存在，则返回 -1 
        return -1
'''
# @lc code=end

