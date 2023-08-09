/*
 * @lc app=leetcode.cn id=20 lang=cpp
 *
 * [20] 有效的括号
 */

// @lc code=start
class Solution {
public:
    bool isValid(string s) {
        if (s.size()%2==1){
            return false;
        }
        stack<char> stk;

        for(int i=0;i<s.size();++i){
            char c=s[i];
            if (c=='('|| c=='{' ||c=='['){
                stk.push(c);
            }
            else{
                if (stk.empty()) return false;
                char top=stk.top();
                if( top == '(' && c == ')' || top == '[' && c == ']' || top == '{' && c == '}' ){
                   // 移除栈顶元素
                   stk.pop();
               }else{
                   // 如果不相同，说明不匹配，返回 false
                   return false;
               }
            }
        }
        return stk.empty();
    }
};
/*
// 登录 AlgoMooc 官网获取更多算法图解
// https://www.algomooc.com
// 作者：程序员吴师兄
// 代码有看不懂的地方一定要私聊咨询吴师兄呀
// 有效的括号（ LeetCode 20 ）:https://leetcode-cn.com/problems/valid-parentheses
class Solution {
public:
    bool isValid(string s) {
        // 当字符串长度为奇数的时候，属于无效情况，直接返回 false
        if (s.size() % 2 == 1) {
             // 无效情况，返回 false
             return false;
        }
       
        //构建一个栈，用来存储括号
        stack<char> stk ;
        
        // 遍历字符串数组中的所有元素
        for( int i = 0 ; i < s.size() ; i++){
            
            // 获取此时的字符
            char c = s[i];   
            
            // 如果字符为左括号 ( ，那么就在栈中添加对左括号 （
            if(c == '('){
               
               // 添加对左括号 （
               stk.push('(');

             // 如果字符为左括号 [ ，那么就在栈中添加对左括号 [
            }else if(c == '['){

               // 添加对应的右括号 ]
               stk.push('[');

             // 如果字符为左括号 { ，那么就在栈中添加对左括号 {
            }else if( c == '{'){

               // 添加对应的右括号 }
               stk.push('{');

               // 否则的话，说明此时 c 是 ）] } 这三种符号中的一种
            }else {
               
               // 如果栈已经为空，而现在遍历的字符 c 是 ）] } 这三种符号中的一种
               // 找不到可以匹配的括号，返回 false
               // 比如这种情况  }{，直接从右括号开始，此时栈为空
               if(stk.empty()) return false;
               
               // 如果栈不为空，获取栈顶元素
               char top = stk.top();

               // 将栈顶元素和此时的元素 c 进行比较，如果相同，则将栈顶元素移除
               if( top == '(' && c == ')' || top == '[' && c == ']' || top == '{' && c == '}' ){
                   // 移除栈顶元素
                   stk.pop();
               }else{
                   // 如果不相同，说明不匹配，返回 false
                   return false;
               }
 
            }

        }
        
        // 遍历完整个字符数组，判断栈是否为空
        // 如果栈为空，说明字符数组中的所有括号都是闭合的
        // 如果栈非空，说明有未闭合的括号
        return stk.empty();

    }
};
*/
// @lc code=end

