/*
 * @lc app=leetcode.cn id=724 lang=cpp
 *
 * [724] 寻找数组的中心下标
 */

// @lc code=start
class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int sum=0;
        for(int x:nums){
            sum+=x;
        }

        int leftSum=0;
        for(int i=0;i<nums.size();++i){
            int rightSum=sum-nums[i]-leftSum;
            if(leftSum==rightSum){
                return i;
            }
            leftSum+=nums[i];
        }
        return  -1;
    }
};

/*
class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        // 先去计算数组所有元素的和
        int sum = 0;

        // 先去计算数组所有元素的和
        for (int x : nums) {

           // 通过累加获取数组所有元素的和
           sum += x;

        }     

        // 假设存在中心下标，那么它的左侧所有元素相加的和是 leftSum
        int leftSum = 0;

        // 从头到尾访问 nums，查看 i 这个索引是否是中心下标
        for (int i = 0; i < nums.size(); i++) {
            
            // 那么 i 这个索引是否是中心下标呢？
            // 取决于其左侧所有元素相加的和等于右侧所有元素相加的和
            // 而右侧所有元素相加的和可以根据总和、i 左侧所有元素相加的和、当前元素的值获取到
            int rightSum = sum - nums[i] - leftSum;

            // 如果发现其左侧所有元素相加的和等于右侧所有元素相加的和
            if ( leftSum == rightSum ) {
                // 找到中心下标了，就是 i
                return i;

            }

            // 否则 i 不是中心下标
            // 那么需要继续去访问，而开始访问下一个元素前，nums[i] 这个元素就要归于 leftSum 了
            leftSum += nums[i];          
        }

        // 遍历结束都没找到结果，说明不存在中心下标，返回 -1
        return -1;
    }
};
*/
// @lc code=end

