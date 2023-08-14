#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 空间复杂度要O(1) 不能O(n)
        # divide-and-conquer algorithm
        count=0
        candidate=0

        for num in nums:
            if count==0:
                candidate=num
            if num==candidate:
                count+=1
            else:
                count-=1 # 一直减，直到==0同归于尽
        return candidate


'''

// 登录 AlgoMooc 官网获取更多算法图解
// https://www.algomooc.com
// 作者：程序员吴师兄
// 代码有看不懂的地方一定要私聊咨询吴师兄呀
// 剑指 Offer 39. 数组中出现次数超过一半的数字 ：https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/
class Solution {
    public int majorityElement(int[] nums) {

        // 统计擂台上擂主的个数
        int count = 0;

        // candidate 表示擂主的编号
        // 一开始，擂台上没有擂主
        int candidate = 0;

        // 数组中的所有数字开始轮番上擂台进行挑战，每个数字的战斗力均为 1
        // 1、相同势力的数字可以都停留在擂台上
        // 2、不同势力的数字会同归于尽
        for (int num : nums) {
            
            // 擂台上没有擂主时
            if (count == 0) {
                // 此时登场的 num 就是擂主
                candidate = num;
            }

            // 擂台上有擂主
            // 并且此时登场的 num 和擂主属于相同的势力
            // 那么两者都停留在场上
            if ( num == candidate){
                count += 1;

            // 否则说明此时登场的 num 和擂主属于不同的势力
            // num 会和一个擂主同归于尽
            }else{
                count -= 1;
            }
           
        }

        // 一轮遍历下来，停留在场上的擂主就是所求的数字
        return candidate;
    }
}
'''
# @lc code=end

