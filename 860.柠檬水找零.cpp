860
/*
 * @lc app=leetcode.cn id=860 lang=cpp
 *
 * [860] 柠檬水找零
 */

// @lc code=start
class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {

    }
};

/*
// 登录 AlgoMooc 官网获取更多算法图解
// https://www.algomooc.com
// 作者：程序员吴师兄
// 代码有看不懂的地方一定要私聊咨询吴师兄呀
// 柠檬水找零（ LeetCode 860 ）:https://leetcode-cn.com/problems/lemonade-change/
class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
         // 用来记录 5 元钞票的数量
        int five = 0;

        // 用来记录 10 元钞票的数量
        int ten = 0;

        // 顾客开始按顺序购买，并找零
        for(int i = 0 ; i < bills.size() ; i++){
            // 1、如果发现是 5 元面额
            if(bills[i] == 5){
                // 那么可以直接收钱，不需要找零
                // 并且 5 元钞票的数量加 1
                five++;

                // 2、如果发现是 10 元面额
            }else if(bills[i] == 10){

                // 如果手中有 5 元钞票，则找零 5 元
                if(five > 0){
                    // 5 元钞票的数量减 1
                    five--;
                    // 10 元钞票的数量加 1
                    ten++;
                }else{
                    // 如果手中没有 5 元钞票，说明找零失败
                    return false;
                }

                // 3、如果发现是 20 元面额
            }else{

                // 如果手中有 10 元 和 5 元钞票，则找零 1 张 10 元和 1 张 5 元的钞票
                if(ten > 0 && five > 0){
                    // 5 元钞票的数量减 1
                    five--;
                    // 10 元钞票的数量减 1
                    ten--;
                }else{
                    // 如果手中只有 5 元的，并且数量超过或者等于 3 张
                    // 那么找零 3 张 5 元的钞票
                    if(five >= 3){
                        // 5 元钞票的数量减 3
                        five -= 3;
                    }else{
                        // 说明这个时候顾客付 20 元的时候
                        // 1、手中没有 1 张 10 元的和 1 张 5 元的
                        // 2、手中没有 3 张 5 元的
                        // 说明找零失败
                        return false;
                    }
                }
            }
        }
        // 所有顾客都找零了，成功
        return true;
    }
};
*/
// @lc code=end

