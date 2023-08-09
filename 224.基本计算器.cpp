/*
 * @lc app=leetcode.cn id=224 lang=cpp
 *
 * [224] 基本计算器
 */

// @lc code=start
class Solution {
public:
    int calculate(string s) {
        stack<int> st;
        int sign=1,res=0,length=s.length();

        for (int i=0;i<length;++i){
            char ch=s[i];
            if(ch>='0' &&ch<='9'){
                long value=ch-'0';

                while(i+1<length && s[i+1]>='0' && s[i+1]<='9'){
                    i++;

                    value=value*10+s[i]-'0';
                }
                res=res+sign*value;
            }
            else if(ch =='+'){
                sign=1;
            }
            else if(ch=='-'){
                sign=-1;
            }
            else if (ch=='('){
                st.push(res);
                res=0;
                st.push(sign);
                sign=1;
            }
            else if(ch==')'){
                int formerSign=st.top();
                st.pop();//先取再弹

                int formerRes=st.top();
                st.pop();
                res=formerRes+formerSign*res;
            }
        }
        return res;
    }
};


/*
// 登录 AlgoMooc 官网获取更多算法图解
// https://www.algomooc.com
// 作者：程序员吴师兄
// 代码有看不懂的地方一定要私聊咨询吴师兄呀
// 基本计算器（ LeetCode 224 ）:https://leetcode-cn.com/problems/basic-calculator
class Solution {
public:
    int calculate(string s) {
        // 使用栈来储存字符串表达式中的数字
        stack<int> st;

        // 为了方便计算，所有的操作都视为加法操作
        // 那么原先的减法操作就相当于是加一个负数
        // 默认都是正数
        int sign = 1;

        // 保存计算的结果
        int res = 0;

        // 获取字符串的长度，然后获取里面的每个字符
        int length = s.length();

        // 获取字符串里面的每个字符
        for(int i = 0;i < length;i++){

            // 获取此时的字符
            char ch = s[i];

            // 如果当前字符是数字的话
            if( ch >= '0' && ch <= '9' ) {
                // 那么可以通过 - '0' 这个操作把字符转换为整数
                // 相当于转换成了 ascii 码进行的数字运算
                long value = ch - '0';

                // 去查看当前字符的后一位是否存在
                // 如果操作并且后一位依旧是数字，那么就需要把后面的数字累加上来
                while (i + 1< length &&s[i+1]>='0'&&s[i+1]<='9'){
                    // i 向后移动，直到遇到非数字为止
                    i++;

                    // i 每向后移动一位，当前的值就需要乘以 10
                    // 比如 s 为 "123+456"
                    // 此时 i = 0，那么 value 为 1
                    // i = 1，那么 value 为 1 * 10 + 2 = 12
                    // i = 2，那么 value 为 12 * 10 + 3 = 123
                     value = value*10 + s[i] - '0';
                     
                }
                // 那么把获取到的数累加到结果 res 上
                res = res + sign * value;

              // 如果是 '+'
            }else if(ch == '+'){
                // 那么说明直接加一个正数
                sign = 1;
              // 如果是 '-'
            }else if(ch == '-'){
                // 那么说明加一个负数
                sign = -1;

              // 如果是 '('
            }else if(ch == '('){
                // 根据数学计算规则，需要先计算括号里面的数字
                // 而什么时候计算呢？
                // 遇到 ) 为止
                // 所以，在遇到 ) 之前需要把之前计算好的结果存储起来再计算
                // ( ) 直接的计算规则和一开始是一样的

                // 1、先把 ( 之前的结果存放到栈中
                st.push(res);

                // 2、重新初始化 res 为 0
                res = 0;

                // 3、把 ( 左边的操作符号存放到栈中
                // 比如如果是 5 - （ 2 + 3 ） ，那么就是把 -1 存放进去
                // 比如如果是 5 +（ 2 + 3 ） ，那么就是把 1 存放进去
                st.push(sign);
                
                // 4、为了方便计算，所有的操作都视为加法操作
                // 那么原先的减法操作就相当于是加一个负数
                // 默认都是正数
                sign = 1;

            // 如果是 ')'
            }else if(ch == ')'){
                // 那么就需要把栈中存放的元素取出来了
                // 在 ch == '（' 这个判断语句中，每次都会往栈中存放两个元素
                // 1、先存放左括号外面的结果
                // 2、再存放左括号外面的符号

                // 1、先获取栈顶元素，即左括号外面的符号，查看是 + 还是 -
                int formerSign = st.top();

                // 把栈顶元素弹出
                st.pop();

                // 2、再获取栈顶元素，即左括号结果
                int formerRes = st.top();

                // 把栈顶元素弹出
                st.pop();

                // 那结果就是括号外面的结果 + 括号里面的结果，至于是加正数还是负数，取决于左括号外面的符号
                res = formerRes +formerSign*res;
            }
        }

        // 返回计算好的结果
        return res;
    }
};
*/
// @lc code=end

