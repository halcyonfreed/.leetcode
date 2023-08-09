/*
 * @lc app=leetcode.cn id=290 lang=cpp
 *
 * [290] 单词规律
 */

// @lc code=start
class Solution {
public:
    bool wordPattern(string pattern, string s) {

    }
};

/*
class Solution {
public:
    bool wordPattern(string pattern, string s) {
        vector<string> words;
        size_t pos = 0;
        string delimiter = " ";
        while ((pos = s.find(delimiter)) != string::npos) {
            words.push_back(s.substr(0, pos));
            s.erase(0, pos + delimiter.length());
        }
        words.push_back(s);

        if (pattern.length() != words.size()) {
            return false;
        }

        vector<string> t;
        for (char c : pattern) {
            t.push_back(string(1, c));
        }

        // 接下来的逻辑和 LC205. 同构字符串 一模一样

        // 设置一个哈希映射用来存储字符串 s 当中的元素
        unordered_map<string, string> dic1;

        // 设置一个哈希映射用来存储字符串 t 当中的元素
        unordered_map<string, string> dic2;

        // 由于 t.size() == words.size()
        // 按照顺序访问 words 和 t 中对应的元素
        for (int i = 0; i < pattern.length(); i++) {
            string word = words[i];
            string patternChar = t[i];

            // 1、访问的元素 word 存在于 dic1 中
            // 并且发现它对应的元素值和当前 t 中元素 patternChar 不相同
            // 返回 false
            if (dic1.count(word) && dic1[word] != patternChar) {
                return false;
            }

            // 2、访问的元素 patternChar 存在于 dic2 中
            // 并且发现它对应的元素值和当前 words 中元素 word 不相同
            // 返回 false
            if (dic2.count(patternChar) && dic2[patternChar] != word) {
                return false;
            }

            // 3、访问的元素 word 不存在于 dic1 中
            // 存放到哈希映射中
            if (!dic1.count(word)) {
                dic1[word] = patternChar;
            }

            // 3、访问的元素 patternChar 不存在于 dic2 中
            // 存放到哈希映射中
            if (!dic2.count(patternChar)) {
                dic2[patternChar] = word;
            }
        }

        // 返回 true
        return true;
    }
};
*/
// @lc code=end

