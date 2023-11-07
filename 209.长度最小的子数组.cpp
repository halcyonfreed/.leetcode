/*
 * @lc app=leetcode.cn id=209 lang=cpp
 *
 * [209] 长度最小的子数组
 */

// @lc code=start
class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        // 暴力解法一
        // int result=INT32_MAX;
        // int sum=0;
        // int subLength=0;

        // for (int i=0;i<nums.size();++i){
        //     sum=0;
        //     for (int j=i; j<nums.size();++j){
        //         sum+=nums[j];
        //         if (sum>=s){
        //             subLength=j-i+1;
        //             result=result>subLength?subLength:result;
        //             break;
        //         }
        //     }
        // }
        // return result==INT32_MAX?0:result;

        // 解法二 sliding window
        int sum=0,subL=0;
        int result=INT32_MAX;
        int i=0;
        for (int j=0;j<nums.size();++j){
            sum+=nums[j];
            while(sum>=target){
                subL=j-i+1;
                result=result<subL?result:subL;

                sum-=nums[i++];
            }
        }
        return result==INT32_MAX?0:result;
    }
};
// @lc code=end
