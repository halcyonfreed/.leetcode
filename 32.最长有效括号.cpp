/*
 * @lc app=leetcode.cn id=32 lang=cpp
 *
 * [32] 最长有效括号
 */

// @lc code=start
class Solution {
public:
    int longestValidParentheses(string s) {

    }
};
/*
// 登录 AlgoMooc 官网获取更多算法图解
// https://www.algomooc.com
// 作者：程序员吴师兄
// 代码有看不懂的地方一定要私聊咨询吴师兄呀
// https://leetcode-cn.com/problems/longest-valid-parentheses/
class Solution {
public:
    int longestValidParentheses(string s) {
        // 利用栈来保留访问路径
        stack<int> stk;

        // maxLength 记录最长有效（格式正确且连续）括号子串的长度
        int maxLength = 0;

        // 设置变量 start 表示合法括号序列的起始索引位置，指向一个左括号，初始值为 0
        int start = 0 ;

        // 1、访问每个字符，假设当前索引为 i，结合访问的元素和栈是否为空，有以下几种情况:
        for(int i = 0 ; i < s.length() ; i++){
            
            // 2、访问到左括号时，不管栈是否为空，都把它存储起来
            if( s[i] == '('){

                stk.push(i);

            // 3、访问到右括号时
            }else{

                // 4、如果当前栈为空，说明这个右括号在前面没有和它匹配的左括号，那么 start 需要发生改变，
                // 下一个访问的字符 i + 1 有可能是左括号，所以 start = i + 1
                if(stk.empty()) {

                    start = i + 1;

                // 5、如果当前栈不为空
                }else{
                    
                    // 6、弹出栈顶元素后
                    stk.pop();

                    // 7、如果栈为空，
                    // 说明以当前右括号为右端点的合法括号序列的左端点为start，则更新长度 i - start + 1
                    if(stk.empty()){

                        maxLength =  max(maxLength,i - start + 1);

                    // 8、如果栈不为空，
                    // 找到了一组合法的括号序列，左括号是刚刚弹出的元素，索引位置可以用栈顶元素索引加 1 获取到，
                    // 那么这组合法括号序列的长度为 i - ( stack.peek() + 1 ) + 1
                    }else{

                        maxLength =  max(maxLength,i - (stk.top() + 1) + 1);

                    }
                }
            }
        }
        return maxLength;
    }
};
*/
// @lc code=end

