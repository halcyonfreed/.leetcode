/*
 * @lc app=leetcode.cn id=242 lang=cpp
 *
 * [242] 有效的字母异位词
 */

// @lc code=start
class Solution {
public:
    bool isAnagram(string s, string t){
        if(s.length()!=t.length()){
            return false;
        }

        vector<int> record(26,0);//26个0

        for(int i=0; i<s.length();++i){
            int index=s[i]-'a';
            record[index]++;
        }

        for(int i=0;i<t.length();++i){
            int index=t[i]-'a';
            record[index]--;

            //减完要是负的 就不行

            if(record[index]<0){
                return false;
            }
        }
        return true;
    }
};

/*
class Solution {
public:
    bool isAnagram(string s, string t) {
        // 如果两个字符串的长度都不一致，那么肯定是无法成为字母异位词的
        if(s.length() != t.length()){

            // 直接返回 false
            return false;

        }

        // 让 a - z 这 26 个字母对应的下标变成 0 - 25 方便存到数组中
        // 比如 a 对应的索引就是 0 
        // b 对应的索引就是 1
        vector<int> table(26, 0);

        // 从头到尾遍历字符串 s
        for( int i = 0 ; i < s.length() ; i++){

            // 把访问的字符转换为整数的形式
            // 比如访问字母 a，那么 -'a' 之后就是 0，就是 a 对应的索引为 0 
            int index = s[i] - 'a';

            // 那么意味着这个字母出现的频次需要加 1
            table[index]++;

        }

        for( int i = 0 ; i < t.length() ; i++){

            // 把访问的字符转换为整数的形式
            // 比如访问字母 a，那么 -'a' 之后就是 0，就是 a 对应的索引为 0 
            int index = t[i] - 'a';

            // 那么意味着这个字母出现的频次需要减 1 
            table[index]--;

            // 如果说发现这个字母出现的频次小于了 0 
            // 说明 t 中出现了 s 中不曾用的字母
            if(table[index] < 0){

                // 那就不是字母异位词
                return false;

            }

        }

        // 否则，说明是字母异位词
        return true;
    }
};
*/
// @lc code=end

