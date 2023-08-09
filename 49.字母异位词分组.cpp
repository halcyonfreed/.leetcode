/*
 * @lc app=leetcode.cn id=49 lang=cpp
 *
 * [49] 字母异位词分组
 */

// @lc code=start
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {

    }
};

/*
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // 互为字母异位词的两个字符串包含的字母相同
        // 因此两个字符串中的相同字母出现的次数一定是相同的
        // 可以将每个字母出现的次数使用字符串表示，作为哈希表的键
        unordered_map<string, vector<string>> mp;

        for (string& str : strs) {
            // counts 代表每个小写字母出现的频次
            vector<int> counts(26);

            // 利用 for 循环，统计 str 当中每个字母出现的频次
            for (char c : str) {
                counts[c - 'a']++;
            }

            // 将每个出现次数大于 0 的字母和出现次数按顺序拼接成字符串，作为哈希表的键
            string key;
            for (int count : counts) {
                key += '#';
                key += to_string(count);
            }

            // 在哈希表 mp 当中找出这个 key 对应的字符串 str 来
            // 1、如果有这个 key，那么这个 key 对应的 数组 会新增一个 str 进去
            // 2、如果没有这个 key，那么会初始化一个数组，用来新增这个 str
            mp[key].emplace_back(str);
        }

        // 返回结果
        vector<vector<string>> res;
        for (auto& p : mp) {
            res.emplace_back(p.second);
        }
        return res;
    }
};
*/
// @lc code=end

