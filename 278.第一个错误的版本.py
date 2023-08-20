#
# @lc app=leetcode.cn id=278 lang=python3
#
# [278] 第一个错误的版本
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # 注意这里不是数组的index，就是index
        left,right =1, n
        while left<right:
            mid=(left+right)//2
            if isBadVersion(mid):
                # 中间是坏的 [mid,right] bad
                right=mid 
            else:
                # [left,mid] good
                left=mid+1
        return left


'''
class Solution {
public:
    int firstBadVersion(int n) {
        // 注意到题目的第一个版本下标为 1 ，所以边界情况为 [ 1 , n ]
        int left = 1 ;
        int right = n ;

        // 利用二分查找的方法，去定位出【第一个错误的版本】
        // 在 while 循环里面，left 不断的 ++，而 right 不断的 --
        // 当 left 和 right 相等， [ left , right ] 这个区间存在一个版本的时候
        // 这个版本就是【第一个错误的版本】
        // 所以，当 left == right 时，跳出循环
        // 此时，while 循环的判断不可以使用等号
        while (left < right) { 
            // left + (right - left) / 2 和 (left + right) / 2 的结果相同
            // 但是使用 left + (right - left) / 2 可以防止由于 left 、right 同时太大，导致相加的结果溢出的问题
            // 比如数据 int 的最大值为 2,147,483,647
            // 此时，left 为 2,147,483,640
            // 此时，right 为 2,147,483,646
            // 两者直接相加超过了 2,147,483,647，产生了溢出
            int mid = left + (right - left) / 2;

            // 调用系统函数，查看当前的版本是否是错误的版本
            // 1、如果当前版本为错误的版本，那么此时 mid 指向的版本有可能是【第一个错误的版本】
            // 因此，区间缩小为 [ left , mid ]
            if (isBadVersion(mid)) {

                // 再次注意，mid 指向的版本有可能是【第一个错误的版本】，因此，right 移动到 mid 的位置
                right = mid;

            // 2、如果当前版本为正确的版本，那么此时 mid 指向的版本绝对不可能是【第一个错误的版本】
            //  因此，区间缩小为 [ mid + 1 , right ]
            } else {
                
                // 再次注意，mid 指向的版本已经是正确的版本了
                // 意味着 [ left , mid ] 的所有版本都是正确的，错误的版本发生在 [ mid + 1 , right ] 这个区间里面
                left = mid + 1; 

            }
        }

        // 当 left 和 right 相等， [ left , right ] 这个区间存在一个版本的时候
        // 这个版本就是【第一个错误的版本】
        return left;
    }
};

'''
# @lc code=end

