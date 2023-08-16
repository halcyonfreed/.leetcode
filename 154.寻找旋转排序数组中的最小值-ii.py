#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right=0,len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]<nums[right]:
                right=mid
            elif nums[mid]>nums[right]:
                left=mid+1
            else:
                right-=1 #不能直接right=mid因为有重复的
        return nums[left] # 不是right
'''
// 登录 AlgoMooc 官网获取更多算法图解
// https://www.algomooc.com
// 作者：程序员吴师兄
// 微信：wzb_3377
// 代码有看不懂的地方一定要私聊咨询吴师兄呀
// 寻找旋转排序数组中的最小值 II（LeetCode 154）：https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array-ii/
class Solution {
    public int findMin(int[] nums) {
        // 搜索区间的左边界
        int left = 0;

        // 搜索区间的右边界
        int right = nums.length - 1;

        // 在搜索区间 [ left , right ] 中去搜索
        // 在 while 里面就可以获取到结果
        while (left < right) {

            // 先去获取搜索区间的中间位置元素
            int mid = left + (right - left) / 2;

         
            // 如果 nums[mid] < nums[right]
            // 最小值一定在 mid 左侧区间或者就是 nums[mid]
            if (nums[mid] < nums[right]) {
                
                // right 移到 mid 的位置。
                right = mid ;

            // 由于 nums 里面的元素存在相同的情况
            // 所以，如果 nums[mid] > nums[right]
            // 最小值一定在 mid 右侧侧区间
            } else if(nums[mid] > nums[right]) {

                // left 移到 mid + 1 的位置。
                left = mid + 1;

            // 如果 nums[mid] = nums[right]
            }else{

                // right 按顺序遍历一样，一个个向左移动 
                // 为什么不能让 right = mid 呢？
                // 给一个测试用例 [3,3,1,3]
                // nums[left] = 3  、 nums[right] = 3 、 nums[mid] = 3
                // 如果让  right = mid，跳过了 1
                right--;

            }
        }

        // 返回结果
        return nums[left];
    }
}
'''

# @lc code=end

