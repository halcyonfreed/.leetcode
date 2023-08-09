/*
 * @lc app=leetcode.cn id=26 lang=cpp
 *
 * [26] 删除有序数组中的重复项
 */

// @lc code=start
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
    //     int n=nums.size(); // .size() vector!!
    //     int j=0; // j是新数组，指向待被赋值的那个
    //     for (int i=0;i<n;++i){
    //         // if (i==0 || nums[i]!=nums[i-1]){
    //         if (i==0 || nums[i]!=nums[j-1]){
    //             nums[j]=nums[i]; //更新nums[j]的值 i遍历nums
    //             j++;
    //         }
    //     }
    //     return j; //就是个数
    // }
    int n=nums.size();
    int j=0;
    for (int i=0;i<n;++i){
        if (i==0 || nums[i]!=nums[j-1]){
            nums[j]=nums[i];
            j++;
        }
        return j;
    }
};
/*
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {

        // 指针 i 进行数组遍历
        int n = nums.size();

        // 指针 j 指向即将被赋值的位置
        int j = 0;

        // 开始对数组进行遍历
        for (int i = 0 ; i < n ; i++) {

            // 进行筛选
            if ( i == 0 ||  nums[i] != nums[i - 1]) {
                // 赋值
                nums[j] = nums[i];

                // j 移动
                j++;
            }
        }

        // 获取结果
        return j ;

    }
};
*/

// @lc code=end

