/*
 * @lc app=leetcode.cn id=485 lang=cpp
 *
 * [485] 最大连续 1 的个数
 */

// @lc code=start
class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        //无标准答案 算法训练营
        int lastZero=-1,ans=0;
        int n=nums.size();
        for (int slow=0;slow<n;++slow){
            if (nums[slow]==0){
                lastZero=slow;
            }
            else{
                ans=max(slow-lastZero,ans);
            }
        }
        return ans;
    }
};
// @lc code=end

