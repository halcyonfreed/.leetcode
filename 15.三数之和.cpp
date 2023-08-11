/*
 * @lc app=leetcode.cn id=15 lang=cpp
 *
 * [15] 三数之和
 */

// @lc code=start
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ans;
        int len=nums.size();
        if (len<3) return ans;

        sort(nums.begin(),nums.end());
        // sort(nums.begin(),nums.begin()+len);

        for (int i=0;i<len;++i){
            if (nums[i]>0) break;
            if (i>0 && nums[i]==nums[i-1]) continue;
            int left=i+1;
            int right=len-1;
            while(left<right){
                int sum=nums[i]+nums[left]+nums[right];
                if (sum==0){
                    vector<int> v={nums[i],nums[left],nums[right]};
                    ans.push_back(v);
                    while (left<right && nums[left]==nums[left+1]) left++;
                    while(left <right && nums)
                }
            }
        }

    }
};


/*

// 登录 AlgoMooc 官网获取更多算法图解
// https://www.algomooc.com
// 作者：程序员吴师兄
// 代码有看不懂的地方一定要私聊咨询吴师兄呀
// 三数之和(15)：https://leetcode-cn.com/problems/3sum/ 
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
  // 题目存在多组解，每一组解都是一个数组，所以使用二维数组存储所有的解
        vector<vector<int>> ans;

        // 获取数组的程度
        int len = nums.size();

        // 边界情况判断
        if(len < 3) return ans;

        // 先将数组进行排序操作，从小到大
        sort(nums.begin(), nums.begin() + len);

        // 开始遍历整个数组
        // 在遍历的过程中，观察设置的三个位置的元素之后的大小
        // num[i] 为从左到右观察过去的元素
        // left 为从 i 到 len - 1 的元素
        // right 为从 len - 1 向左移动到 i 的元素
        for (int i = 0; i < len ; i++) {

            // 如果发现 nums[i] > 0 ，由于 nums 是递增序列，left 在 nums[i] 的右侧，right 也在 nums[i] 的右侧
            // 那么 num[i]、nums[left]、nums[right] 都大于 0 
            // 说明这三数之和一定大于 0 ，结束循环
            if(nums[i] > 0) break; 

            // 答案中不可以包含重复的三元组，所以需要执行一个去重的操作
            // 比如这个输入 [-4,-1,-1,0,1,2]
            // i 指向的为第一个 -1 时，left 指向的元素值为 0 ，right 指向的元素值为 1 
            // i 指向的为第二个 -1 时，left 指向的元素值为 0 ，right 指向的元素值为 1 
            // 这两组解都是 [ -1 , 0 , 1]，所以需要去重
            if(i > 0 && nums[i] == nums[ i - 1 ]) continue; 

            // left 为从 i 到 len - 1 的元素，向右移动
            int left = i + 1;

            // right 为从 len - 1 向左移动到 i 的元素，向左移动
            int right = len - 1;

            // left 和 right 不断的向内移动
            while(left < right){

                // 计算这三者之和
                int sum = nums[i] + nums[left] + nums[right];

                // 发现三者之和为 0
                if(sum == 0){

                    // 把这个结果记录一下
     vector<int>v = {nums[i], nums[left], nums[right]};
     ans.push_back(v);
     
                    // 答案中不可以包含重复的三元组，所以需要执行一个去重的操作
                    // 比如这个输入 [-2,0,0,2,2]
                    // i 指向的元素值为 -2 ，left 指向的元素值为第一个 0 ，right 指向的元素值为倒数第一个 2 时
                    // 它们的 sum 为 0 ，如果让 ，left 向右移动一下，，right 向左移动一下，它们的 sum 也为 0
                    // 但是这两组解都是 [ -2 , 0 , 2]，所以需要去重
                    while( left < right && nums[left] == nums[ left + 1 ]) {
                        // left 向右移动
                        left++;
                    }

                    while( left < right && nums[right] == nums[ right - 1]){
                        // right 向左移动
                        right--;
                    }

                    // left 向右移动
                    left++;

                    // right 向左移动
                    right--;

                // 如果三者之和小于 0 ，那么说明需要找更大的数
                }else if (sum < 0){
                    // left 向右移动
                    left++;

                // 如果三者之和大于 0 ，那么说明需要找更小的数
                }else if (sum > 0) {
                    // right 向左移动
                    right--;
                }
            }
        }     
        // 返回结果   
        return ans;
    }
};
*/
// @lc code=end

