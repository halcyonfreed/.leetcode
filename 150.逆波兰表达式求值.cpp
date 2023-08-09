/*
 * @lc app=leetcode.cn id=150 lang=cpp
 *
 * [150] 逆波兰表达式求值
 */

// @lc code=start
class Solution {
public:
    int evalRPN(vector<string>& tokens){
        stack<int> result;

        long int rightNum,leftNum,ans;
        for (int i=0; i<tokens.size();++i){
            if(tokens[i] == "+" || tokens[i] == "-" || tokens[i] == "*" || tokens[i] == "/" ){
                rightNum=result.top();
                result.pop();
                leftNum=result.top();
                result.pop();
            }
            if(tokens[i] == "+") ans=leftNum+rightNum;
            else if(tokens[i] == "*") ans=leftNum*rightNum;
            else if(tokens[i] == "/") ans=leftNum/rightNum;
            else if(tokens[i] == "-") ans=leftNum-rightNum;
            // else ans=int(tokens[i]); //不行
            else ans=stoi(tokens[i]);

            result.push(ans);
        }
        return result.top();
}
};
/*
class Solution {
public:
    int evalRPN(vector<string>& tokens) {

        // 使用一个栈存储操作数，从左到右遍历逆波兰表达式
        stack<int> result;

        // 对于一个表达式来说，由两个操作数和一个运算符构成
        // 比如加法：① ＋ ②
        // 比如减法：① -  ②
        // 比如乘法：① *  ②
        // 比如除法：① /  ②

        // 先出栈的是右操作数，后出栈的是左操作数

        // 先出栈的是右操作数
        long int rightNum;

        // 后出栈的是左操作数
        long int leftNum;

        // 一个表达式的计算结果
        long int ans;

        // 遍历字符串数组
        for (int i = 0; i < tokens.size(); i++) {

            // c++没有in这种！！    如果是 + 
            if(tokens[i] == "+"){

                // 先出栈的是右操作数
                rightNum = result.top();

                result.pop();

                // 后出栈的是左操作数
                leftNum = result.top();

                result.pop();

                // 计算结果
                ans = leftNum + rightNum;

            // 如果是 - 
            }else if(tokens[i] == "-"){

                // 先出栈的是右操作数
                rightNum = result.top();

                result.pop();

                // 后出栈的是左操作数
                leftNum = result.top();

                result.pop();

                // 计算结果
                ans = leftNum - rightNum;    

            // 如果是 *
            }else if(tokens[i] == "*"){

                // 先出栈的是右操作数
                rightNum = result.top();

                result.pop();

                // 后出栈的是左操作数
                leftNum = result.top();

                result.pop();

                // 计算结果
                ans = leftNum * rightNum; 

            // 如果是 /
            }else if(tokens[i] == "/"){

                // 先出栈的是右操作数
                rightNum = result.top();

                result.pop();

                // 后出栈的是左操作数
                leftNum = result.top();

                result.pop();

                // 计算结果
                ans = leftNum / rightNum; 

            // 如果是非运算符
            }else{
                
                // 转换为数字
                ans = stoi(tokens[i]);
                
            }

            // 存储结果
            result.push(ans);

        }

        // 返回栈顶元素
        return result.top();

    }
};
*/
// @lc code=end

