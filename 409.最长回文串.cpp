/*
 * @lc app=leetcode.cn id=409 lang=cpp
 *
 * [409] 最长回文串
 */

// @lc code=start
class Solution {
public:
    int longestPalindrome(string s) {
        int cnt[58]={0};  //长度58 都是0
        
        // string::size_type它是一个无符号类型的值，而且能够存放下任何string对象的大小。另外，string类型的索引也是一个size_type类型的。下标运算符 [ ] 接收的就是string::size_type类型。
        for(string::size_type i = 0; i < s.size(); i++) {
        // for(int i=0;i<s.size();++i){
            if('a'<=s[i] &&s[i]<='z'){
                cnt[s[i]-'a']++;
            }else{
                cnt[s[i]-'A'+26]++;
            }
        }

        int ans=0;

        for(int x:cnt){
            //遍历cnt
            ans+=x-(x&1);
        };

        return ans<s.length()? ans+1:ans;
}
};

/*
class Solution {
public:
    int longestPalindrome(string s) {

        // 手动设置哈希表，哈希函数为 c - 'A'
        // 这里的哈希表的作用是计数器
        // 由于 大写字母 'A' 与小写字母 'a' 的 ASCII 相差 32
        // A : 65
        // a : 97
        // 所以设置哈希表的大小为 32 + 26 = 58
        // 因为用数字替代了字母，所以65-90 A-Z； 97-122 a-z  当中90-96是空掉了
        int cnt[58] = {0};

        // 统计每个字母出现的频次
        for(string::size_type i = 0; i < s.size(); i++) {
            if('a' <= s[i] && s[i] <= 'z') {
                cnt[s[i]-'a']++;
            } else {
                cnt[s[i]-'A'+26]++;
            }
        }

        // 初始化结果
        int ans = 0;

        for (int x: cnt) {

            // 根据奇偶性来判断当前字母的使用次数为多少   
            // 按位与：& 
            // 将参与运算的两操作数各对应的二进制位进行与操作
            // 只有对应的两个二进位均为 1 时，结果的对应二进制位才为 1 ，否则为 0
            // 通过这个方法判断 x 的奇偶性，即统计这个字母出现的是偶数次还是奇数次
            // 1 的二进制为          0001 
            // 比如 x 为 4，二进制为  0100 ，那么 x & 1 的结果是 0000 ，即为 0
            // 那么 x -  (x & 1) 的结果是 4，那么这 4 个字母全部都可以出现在最终的回文串中
            // **********
            // 比如 x 为 5，二进制为  0101 ，那么 x & 1 的结果是 0001 ，即为 1
            // 那么 x -  (x & 1) 的结果是 4，即出现了 5 次的那个字母只有其中 4 个可以被用上
            ans += x - (x & 1);

        }

        // 最后，会尝试一下，能不能再添加一个字符到回文串中
        // 如果最终的长度小于原字符串的长度，说明里面某个字符出现了奇数次，那么那个字符可以放在回文串的中间，所以额外再加一
        return ans < s.length() ? ans + 1 : ans; 

    }
};
*/
// @lc code=end

