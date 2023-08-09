/*
 * @lc app=leetcode.cn id=283 lang=cpp
 *
 * [283] 移动零
 */

// @lc code=start
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int slow=0;
        int n=nums.size();
        for (int fast=0;fast<n;++fast){
            if (nums[fast]!=0){
                nums[slow]=nums[fast];
                slow++;
            }
        }
        for (int i=slow;i<n;++i){
            nums[i]=0;
        }
    }
};
/*class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        // 设置一个变量，用来指向经过一系列操作后数组中所有为 0 元素的第一个位置上
        // 一开始默认在索引为 0 的位置
        int slow = 0;

        // 从头到尾遍历数组
        // 遍历完毕之后，slow 指向了一个为 0 的元素，或者如果数组中不存在 0 ，就和 fast 一样，超过了数组的范围
        for (int fast = 0; fast < nums.size(); fast++) {

            // 在遍历过程中，如果发现访问的元素是非 0 元素
            // 说明 slow 不在正确的位置上，需要向后移动，寻找合适的位置
            if (nums[fast] != 0) {

                // 这个时候，原先 slow 的值需要被 fast 的值覆盖
                nums[slow] = nums[fast];

                // slow 需要向后移动，寻找合适的位置
                slow++;

            }
        }

        // 接下来，只需要把 slow 极其后面所有的元素都设置为 0 就行
        for (int i = slow; i < nums.size(); i++) {

            // 都设置为 0 
            nums[i] = 0;

        }
    }
};*/
// @lc code=end

