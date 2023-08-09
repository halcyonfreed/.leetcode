/*
 * @lc app=leetcode.cn id=383 lang=cpp
 *
 * [383] 赎金信
 */

// @lc code=start
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        vector<int> cnt(26,0);
        
        // for (auto &c:magazine){
        for (auto c:magazine){
            cnt[c-'a']++;
        }
        // for(auto c:ransomNote){
        for(auto c:ransomNote){
            cnt[c-'a']--;
            if (cnt[c-'a']<0){
                return false;
            }
        }
        return true;
    }
};
/*
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {

        // 手动设置哈希表
        // 这里的哈希表的作用是计数器
        // 由于小写字母的个数为 26 个，所以数组大小为 26
        vector<int> cnt(26);


        // 记录 magazine 里字母出现的次数
        for (auto & c : magazine) {
            cnt[c - 'a']++;
        }
        
        // 再用 ransomNote 去验证这个数组是否包含了 ransomNote 所需要的所有字母
        for (auto & c : ransomNote) {
            // 在遍历过程中，每遍历一个字母，对应的频次减 1
            cnt[c - 'a']--;

            // 如果发现某个字母的频次小于了 0
            // 说明在 ransomNote 中出现了 magazine 未曾有的字母
            // 即 ransomNote 不能由 magazine 里面的字符构成
            if(cnt[c - 'a'] < 0) {

                // 返回 false 
                return false;
            }
        }

        // 说明可以，返回 true 
        return true;

    }
};
*/
// @lc code=end

