#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp=collections.defaultdict(list)

        for s in strs:
            counts=[0]*26

            for c in s:
                counts[ord(c) - ord('a')] += 1
            key = ''.join(['#'+str(count) for count in counts])
            mp[key].append(s)
        return list(mp.values())
            

'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 互为字母异位词的两个字符串包含的字母相同
        # 因此两个字符串中的相同字母出现的次数一定是相同的
        # 可以将每个字母出现的次数使用字符串表示，作为哈希表的键
        mp = collections.defaultdict(list)

        for s in strs:
            # counts 代表每个小写字母出现的频次
            counts = [0] * 26

            # 利用 for 循环，统计 str 当中每个字母出现的频次
            for c in s:
                counts[ord(c) - ord('a')] += 1

            # 将每个出现次数大于 0 的字母和出现次数按顺序拼接成字符串，作为哈希表的键
            key = ''.join(['#'+str(count) for count in counts])

            # 在哈希表 mp 当中找出这个 key 对应的字符串 str 来
            # 1、如果有这个 key，那么这个 key 对应的 数组 会新增一个 str 进去
            # 2、如果没有这个 key，那么会初始化一个数组，用来新增这个 str
            mp[key].append(s)

        # 返回结果
        return list(mp.values())
'''

# @lc code=end

