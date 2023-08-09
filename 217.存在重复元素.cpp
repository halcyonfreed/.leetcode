/*
 * @lc app=leetcode.cn id=217 lang=cpp
 *
 * [217] 存在重复元素
 */

// @lc code=start
class Solution {
public:
    bool containsDuplicate(vector<int>& nums){
        unordered_set<int> s;
        for (int x:nums){
            if (s.find(x)!=s.end()){
                return true;
            }
            s.insert(x);
        }
        return false;
    }
};

/*
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {

        // 使用数据结构 unordered_set 来存放 nums 里面的所有数字
        unordered_set<int> s;

        // 遍历数组 
        for (int x: nums) {

            // 如果数字已经存在于 set 中，直接返回 true 
            if (s.find(x) != s.end()) {
                return true;
            }

            // 把元素添加到 set 中
            s.insert(x);
        }

        // 如果成功遍历完数组，则表示没有重复元素，返回 false
        return false;
    }
};
*/
// @lc code=end

