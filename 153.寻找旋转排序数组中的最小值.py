#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right=0,len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]<nums[right]:
                right=mid # 不是mid-1
            else:
                left=mid+1
        # return nums[right] # 这里why返回的是right
        return nums[left] # left也可以while跳出来的条件是==
'''
// 登录 AlgoMooc 官网获取更多算法图解
// https://www.algomooc.com
// 作者：程序员吴师兄
// 微信：wzb_3377
// 代码有看不懂的地方一定要私聊咨询吴师兄呀
// 寻找旋转排序数组中的最小值（LeetCode 153）：https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/ 
class Solution {
    public int findMin(int[] nums) {

        // 搜索区间的左边界
        int left = 0;

        // 搜索区间的右边界
        int right = nums.length - 1;

        // 在搜索区间 [ left , right ] 中去搜索
        // 在 while 里面就可以获取到结果
        while ( left < right ) {

            // 先去获取搜索区间的中间位置元素
            int mid = left + (right - left) / 2;

            // 如果 nums[mid] < nums[right]
            // 最小值一定在 mid 左侧区间或者就是 nums[mid]
            if (nums[mid] < nums[right]) {
                
                // right 移到 mid 的位置。
                // 疑问：为什么 right = mid ; 而不是 right = mid - 1;
        // 解答：{4,5,1,2,3}，如果 right = mid - 1 ，则丢失了最小值 1
                right = mid;

            // 由于 nums 里面的元素都互不相同
            // 所以，如果 nums[mid] > nums[right]
            // 最小值一定在 mid 右侧侧区间
            } else {

                // left 移到 mid + 1 的位置。
                // 疑问：为什么 left = mid + 1 ;而不是 left = mid;
        // 解答：{4,5,6,1,2,3}，nums[mid] = 6，left = mid + 1 ,刚好 nums[left] = 1
                left = mid + 1;
            }
        }

        // 返回结果
        return nums[right];

    }
}
'''
# @lc code=end

