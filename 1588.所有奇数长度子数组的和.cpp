/*
 * @lc app=leetcode.cn id=1588 lang=cpp
 *
 * [1588] 所有奇数长度子数组的和
 */

// @lc code=start
class Solution {
public:
    int sumOddLengthSubarrays(vector<int>& arr) {
        int ans=0;
        vector<int> preSum(arr.size()+1,0); //长度arr.size()+1，都是0
        // preSum[ i ] 表示数组 nums 从下标 0 到下标 i - 1 的所有元素之和

        for (int i=0;i<arr.size();++i){
            preSum[i+1]=preSum[i]+arr[i];
        }

        // 从索引为 0 的位置开始遍历出所有，j= 1、3、5 等等奇数长度的子数组
        for(int i=0;i<arr.size();++i){
            for (int j=1;j<=arr.size();j+=2){
                if(i+j-1<arr.size()){
                    ans+=preSum[i+j]-preSum[i];
                }
            }
        }
        return ans;
    }
};
/*
class Solution {
public:
    int sumOddLengthSubarrays(vector<int>& arr) {
        int ans = 0;
        vector<int> preSum(arr.size() + 1, 0);

        for (int i = 0; i < arr.size(); i++) {
            preSum[i + 1] = preSum[i] + arr[i];
        }

        for (int i = 0; i < arr.size(); i++) {
            for (int j = 1; j <= arr.size(); j += 2) {
                if (i + j - 1 < arr.size()) {
                    ans += preSum[i + j] - preSum[i];
                }
            }
        }

        return ans;
    }
};

*/
// @lc code=end

