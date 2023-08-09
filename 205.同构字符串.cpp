/*
 * @lc app=leetcode.cn id=205 lang=cpp
 *
 * [205] 同构字符串
 */

// @lc code=start
class Solution {
public:
    bool isIsomorphic(string s, string t) {

    }
};
/*


class Solution {
public:
    bool isIsomorphic(string s, string t) {
        // 创建哈希映射用于存储字符串s中的元素
        unordered_map<char, char> map1;
        
        // 创建哈希映射用于存储字符串t中的元素
        unordered_map<char, char> map2;

        // 由于t.length == s.length
        // 按顺序访问s和t中对应的元素
        for (int i = 0; i < s.length(); i++) {
            char charS = s[i];
            char charT = t[i];

            // 1. 如果元素charS已经存在于map1中
            // 并且对应的值与当前元素charT不相同，返回false
            if (map1.count(charS) && map1[charS] != charT) {
                return false;
            }

            // 2. 如果元素charT已经存在于map2中
            // 并且对应的值与当前元素charS不相同，返回false
            if (map2.count(charT) && map2[charT] != charS) {
                return false;
            }

            // 3. 如果元素charS不存在于map1中，将其放入哈希映射中
            if (!map1.count(charS)) {
                map1[charS] = charT;
            }

            // 4. 如果元素charT不存在于map2中，将其放入哈希映射中
            if (!map2.count(charT)) {
                map2[charT] = charS;
            }
        }

        // 返回true
        return true;
    }
};


*/
// @lc code=end

