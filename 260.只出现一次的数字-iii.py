#
# @lc app=leetcode.cn id=260 lang=python3
#
# [260] 只出现一次的数字 III
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        sum=0
        for num in nums:
            sum^=num
        

        k=sum==-sys.maxint-1 ? sum:sum & -sum

        a,b=0,0


'''
java:
// 登录 AlgoMooc 官网获取更多算法图解
// https://www.algomooc.com
// 作者：程序员吴师兄
// 代码有看不懂的地方一定要私聊咨询吴师兄呀
// 只出现一次的数字 III（ LeetCode 260 ）：https://leetcode-cn.com/problems/single-number-iii/
class Solution {
    public int[] singleNumber(int[] nums) {
        
        // sum 表示数组 nums 所有元素进行异或的结果
        int sum = 0;

        // 遍历 nums 中的每个元素
        for (int num : nums){

            // 将每个元素都执行异或操作
            sum ^= num;

        } 

        // 1、由于 nums 中其余元素均出现两次
        // 2、异或的特征：不同为 1 ，相同为 0 
        // 因此，最终的 sum 就是那两个只出现一次的元素异或的结果
        // 假设这两个只出现一次的元素分别为 a 和 b
        // a = 011 , b = 101 , 那么 sum = 110
        // 也就意味着 sum 上面的 1 必然是由 a 与 b 贡献的，因为两个相同元素的二进制必然相同，异或一下为 0
        // 假设 sum 上面的第 k 位是 1
        // 那么，我们可以将 nums 划分为两部分数组
        // 1、第 k 位是 1，包含了 b 与 nums 中第 k 位是 1 的元素，并且这些元素出现了两次
        // 2、第 k 位是 0，包含了 a 与 nums 中第 k 位是 0 的元素，并且这些元素出现了两次
        // 也就是说，a 与 b 划分到了不同的部分
        // 而相同的元素进行异或为 0 ，那么每一部分进行异或最终就剩下了一个只出现一次的元素

        // 先去找出 sum 中任意一位为 1 的位置，我们这里去找最低位为 1 的位置
        // sum & -sum 的结果是 nsum的最低位的二进制
          // 比如 sum = 1011，那么它的反码是 0100，补码就是 0101
          // sum =            1011
          // &
          // -sum =           0101
          // ------------------------
          // 结果就是   0001
          // 即获取到了 sum 中最低位为 1 的位置
          // 实际上也可以这样理解，-sum 是 sum 取反再加 1 ，那么 sum & -sum 取得的就是再加的那个 1
          // 特殊情况，如果 sum =  Integer.MIN_VALUE，即 sum = -2^31
          // Integer.MIN_VALUE，即 -2147483648，二进制位如下： 
          // 1000 0000 0000 0000 0000 0000 0000 0000
          // 取反后再加 1 会产生溢出的情况
        int k = (sum == Integer.MIN_VALUE) ? sum  : sum & -sum;

        // 假设这两个只出现一次的元素分别为 a 和 b
        int a = 0;

        // 假设这两个只出现一次的元素分别为 a 和 b
        int b = 0;

        // 再次遍历 nums ，将 num 划分为两部分
        for(int num:nums){

            // 这部分表示第 k 位为 0 的元素，包含了 a 与 nums 中第 k 位是 0 的元素，并且这些元素出现了两次
            if( ( k & num ) == 0 ){

                // 这些元素进行异或，最终剩下了那个只出现一次的元素 a
                a ^= num;

            // 这部分表示第 k 位为 1 的元素，包含了 b 与 nums 中第 k 位是 1 的元素，并且这些元素出现了两次
            }else{

                // 这些元素进行异或，最终剩下了那个只出现一次的元素 b
                b ^= num;

            }        
        }

        // 结合为数组的形式进行返回
        int ans[] = { a , b } ;

        // 返回结果
        return ans;
    }
}
'''
# @lc code=end

