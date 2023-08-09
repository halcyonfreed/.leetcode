/*
 * @lc app=leetcode.cn id=303 lang=cpp
 *
 * [303] 区域和检索 - 数组不可变
 */

// @lc code=start
class NumArray {
public:
    // 定义前缀和数组
    vector<int> sums;
    
    NumArray(vector<int>& nums) {
        int n=nums.size();
        sums.resize(n+1);
       
        for(int i=0;i<n;++i){
            // sums[ i ] 表示数组 nums 从下标 0 到下标 i - 1 的所有元素之和
            // 初始化 sums 数组
            sums[i+1]=sums[i]+nums[i];
        }
    }
    
    int sumRange(int left, int right) {
        return sums[right+1]-sums[left];
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */
// @lc code=end

