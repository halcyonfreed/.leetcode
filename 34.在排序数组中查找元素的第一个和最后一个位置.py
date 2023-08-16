#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        firsIdx=self.findFP(nums,target)
        endIdx=self.findEP(nums,target)
        return [firsIdx,endIdx]
    def findFP(self,nums:List[int],target:int)->int:
        left,right=0,len(nums)-1

        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                if mid==0 or nums[mid-1]<target:
                    return mid
                right=mid-1

            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return -1
    def findEP(self,nums:List[int],target:int)->int:
        left,right=0,len(nums)-1

        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                if mid==len(nums)-1 or nums[mid+1]>target:
                    return mid
                left=mid+1

            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return -1
'''
class Solution {
    public int[] searchRange(int[] nums, int target) {
        
        // 寻找目标值在数组中的开始位置
        int firstIdx = findBeginPostion(nums,target);

        // 寻找目标值在数组中的结束位置
        int lastIdx = findEndPostion(nums,target);

        // 返回寻找的结果
        return new int[]{firstIdx,lastIdx};

    }

    // 寻找目标值在数组中的开始位置
    private int findBeginPostion(int[] nums , int target){

        // left 指向当前区间的最左边位置，所以初始化为 0
        int left = 0;

        // right 指向当前区间的最右边位置，所以初始化为 nums.length - 1
        int right = nums.length - 1;

        // 循环进行二分查找，直到左端点位置超过了右端点
        // 或者在循环过程中找到了起始位置
        while(left <= right){

            // 计算当前区间的中间位置，向下取整
            int mid = (left + right) / 2;

            // 如果中间位置的元素值等于目标值 target
            if(nums[mid] == target){

                // 并且中间位置 mid 的左边没有元素，即中间位置 mid 为当前区间的起始位置
                // 或者中间位置 mid 的前一个元素小于目标值 target
                // 说明 mid 指向了 target 的起始位置
                if(mid == 0 || nums[mid - 1] < target){
                    // mid 指向了 target 的起始位置，返回这个结果
                    return mid;
                }

                // 否则，说明 mid 的左边依然有元素值等于 target
                // 那么 mid 就不是 target 的起始位置，需要在 mid 的左边进行查找
                // 所以缩小范围为 left 到 mid - 1
                // 当前区间的左侧为 left，右侧 right = mid - 1
                right = mid - 1;

            // 如果中间位置的元素值大于目标值 target
            // 说明需要在 mid 的左边进行查找
            }else if( nums[mid] > target){

                // 所以缩小范围为 left 到 mid - 1
                // 当前区间的左侧为 left，右侧 right = mid - 1
                right = mid - 1;

            // 如果中间位置的元素值小于目标值 target
            // 说明需要在 mid 的右边进行查找
            }else{

                // 所以缩小范围为 mid + 1 到 right
                // 当前区间的左侧为 left = mid + 1，右侧 right 
                left = mid + 1;

            }
        }
        
        // 如果循环结束后还没有返回，说明找不到目标值 target，返回 -1
        return - 1;
    }

    // 寻找目标值在数组中的结束位置
    private int findEndPostion(int[] nums , int target){

        // left 指向当前区间的最左边位置，所以初始化为 0
        int left = 0;

        // right 指向当前区间的最右边位置，所以初始化为 nums.length - 1
        int right = nums.length - 1;

        // 循环进行二分查找，直到左端点位置超过了右端点
        // 或者在循环过程中找到了结束位置    
        while(left <= right){

            // 计算当前区间的中间位置，向下取整
            int mid = (left + right) / 2;

            // 如果中间位置的元素值等于目标值 target
            if(nums[mid] == target){
                // 并且中间位置 mid 的右边没有元素，即中间位置 mid 为当前区间的结束位置
                // 或者中间位置 mid 的后一个元素大于目标值 target
                // 说明 mid 指向了 target 的结束位置
                if(mid == nums.length - 1 || nums[mid + 1] > target){
                    // mid 指向了 target 的结束位置，返回这个结果
                    return mid;
                }

                // 否则，说明 mid 的右边依然有元素值等于 target
                // 那么 mid 就不是 target 的结束位置，需要在 mid 的右边进行查找
                // 所以缩小范围为 mid + 1 到 right
                // 当前区间的左侧为 left = mid + 1 ，右侧为 right 
                left = mid + 1;

            // 如果中间位置的元素值大于目标值 target
            // 说明需要在 mid 的左边进行查找
            }else if( nums[mid] > target){

                // 所以缩小范围为 left 到 mid - 1
                // 当前区间的左侧为 left，右侧 right = mid - 1
                right = mid - 1;

            // 如果中间位置的元素值小于目标值 target
            // 说明需要在 mid 的右边进行查找
            }else{

                // 所以缩小范围为 mid + 1 到 right
                // 当前区间的左侧为 left = mid + 1，右侧 right 
                left = mid + 1;

            }
        }

        // 如果循环结束后还没有返回，说明找不到目标值 target，返回 -1
        return - 1;    
    }

}
'''
# @lc code=end

