#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 轮转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k%=len(nums) # k比数组长，就需要取余
        self.reverse(nums,0,len(nums)-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,len(nums)-1)

    def reverse(self,nums:List[int],left:int,right:int)->None:
        # two-pointers用了双指针inplace 来遍历替换; 交换两个值
        while left<right:
            temp=nums[left]
            nums[left]=nums[right]
            nums[right]=temp
            left+=1
            right-=1
    

'''
只有Java 没有python cpp
// 登录 AlgoMooc 官网获取更多算法图解
// https://www.algomooc.com
// 作者：程序员吴师兄
// 添加微信 278166530 获取最新课程
// 代码有看不懂的地方一定要私聊咨询吴师兄呀
// LeetCode 189、轮转数组：https://leetcode.cn/problems/rotate-array/
class Solution {
    public void rotate(int[] nums, int k) {

        // 1、对 k 进行取余操作
        k %= nums.length;

        // 第一步，翻转整个数组
        reverse(nums, 0, nums.length - 1);
        // 第二步，翻转前 k 个元素
        reverse(nums, 0, k - 1);
        // 第三步，翻转后面的所有元素
        reverse(nums, k, nums.length - 1);
    }

    // 翻转区间 [ start , end ] 里面的元素
    public void reverse(int[] nums, int start, int end) {
        while (start < end) {
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start += 1;
            end -= 1;
        }
    }
}
'''
# @lc code=end

