/*
 * @lc app=leetcode.cn id=27 lang=cpp
 *
 * [27] 移除元素
 */

// @lc code=start
// class Solution {
// public:
//     int removeElement(vector<int>& nums, int val) {
//         int slow=0;
//         // int n=nums.size(); 注释掉比不注释慢很多！！
//         for (int i =0; i<nums.size();++i){
//             if (nums[i]!=val){
//                 nums[slow]=nums[i];
//                 slow++;
//             }            
//         }
//         return slow;
//     }
// };

class Solution{
public:
    int removeElement(vector<int>& nums, int val){
        int slow=0;
        for (int fast=0;fast<nums.size();fast++){
            if (nums[fast]!=val){
                nums[slow]=nums[fast];
                slow++;
            }
        }
        return slow;
    }
};
// @lc code=end

