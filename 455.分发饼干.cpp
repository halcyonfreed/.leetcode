/*
 * @lc app=leetcode.cn id=455 lang=cpp
 *
 * [455] 分发饼干
 */

// @lc code=start
class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        //典型的开心算法 已从小到大排序了
        sort(g.begin(),g.end());
        sort(s.begin(),s.end());

        int child=0,cookie=0;

        while (cookie<s.size() && child<g.size()){
            if( s[cookie]>=g[child]){
                child++;
            }
            cookie++;
        }
        return child;
    }
};

/*

// 登录 AlgoMooc 官网获取更多算法图解
// https://www.algomooc.com
// 作者：程序员吴师兄
// 代码有看不懂的地方一定要私聊咨询吴师兄呀
// 分发饼干（ LeetCode 455 ）:https://leetcode-cn.com/problems/assign-cookies/
class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        // 1、将孩子们的胃口值按照从小到大的顺序排列
        // 优先满足胃口小的孩子
        sort(g.begin(), g.end());

        // 2、将饼干按照从小到大的顺序排列
        sort(s.begin(), s.end());

        // child 代表 g 的下标，即表示有多少孩子的胃口得到满足
        int child = 0;

        // child 代表 s 的下标，即表示目前有多少饼干被使用了
        int cookie = 0;

        // 遍历所有的饼干
        // 遍历过后，饼干只有两种状态
        // 1、要么找到了需要这个饼干的孩子
        // 2、要么剩下的孩子中，胃口值最低的孩子都大于这个饼干的值，那么这个饼干没人要
        while(cookie < s.size() && child < g.size()){

            // 孩子的胃口得到了满足
            if(s[cookie] >= g[child]){
                // 得到满足的孩子数量加 1
                child++;
            }

            // 查看下一个饼干能否找到需要的孩子
            cookie++;
        }

        // 最后返回孩子数量
        return child;
    }
};

*/
// @lc code=end

