/*
 * @lc app=leetcode.cn id=560 lang=cpp
 *
 * [560] 和为 K 的子数组
 */

// @lc code=start
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int count=0;
        int pre=0;

        unordered_map<int,int> mp;

        mp[0]=1; // 为了防止只有一个那种

        for (int i=0;i<nums.size();++i){
            pre+=nums[i];
            // != .end()代表 .end()前面能找到前缀和是pre-k
            if (mp.find(pre-k)!=mp.end()){
                count+=mp[pre-k]; 
            }

            mp[pre]++; // 出现的次数
        }
        return count;
    }
};

/*
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {

        // 统计和为 K 的子数组的数量
        int count = 0;
        
        // 记录遍历到索引为 i 的这个元素时，前缀和的值是多少
        int pre = 0;

        // 利用哈希表，以前缀和为键，出现次数为对应的值，记录 pre[i] 出现的次数 
        unordered_map<int, int> mp;
        
        // 一开始，需要设置前缀和为 0 时，出现的次数为 1 次
        // 这一行的作用就是为了应对 nums[0] +nums[1] + ... + nums[i] == k 这种情况
        // 如数组 [1, 2, 3, 6]
        // 这个数组的累加和数组为 [1, 3, 【6】, 12] 
        // 如果 k = 6, 假如 mp 中没有预先存储(0, 1) 
        // 那么来到累加和为 6 的位置时，这时 mp 中存储的就只有两个数据 (1, 1), (3, 1)
        // 想去判断 mp.containsKey(pre - k) , 这时 pre - k = 6 - 6 = 0
        // 但 map 中没有 (0, 1) ，
        // 因为这个时候忽略了从下标 0 累加到下标 i 等于 k 的情况
        // 仅仅是统计了从下标大于 0 到某个位置等于 k 的所有答案
        mp[0] =  1;

        // 开始从头到尾遍历 nums 数组，在遍历过程中，会执行两个操作
        // 1、存储索引为 i 的这个元素时，前缀和的值是多少，并且把这个值出现的频次存储到 mp 中
        // 2、判断之前有没有存储 pre - k 这种前缀和，如果有，说明 pre - k 到 pre 直接的那些元素值之和就是 k
        for (int i = 0; i < nums.size(); i++) {

            // 存储索引为 i 的这个元素时，前缀和的值是多少
            pre += nums[i];

            // 判断之前有没有存储 pre - k 这种前缀和
            if (mp.find(pre - k) != mp.end()) {

                // 如果有，说明 pre - k 到 pre 直接的那些元素值之和就是 k
                // 找到了一组，累加到 count 上
                count += mp[pre - k];

            }

            // 这个值出现的频次存储到 mp 中
            mp[pre]++;
        }

        // 返回结果
        return count;

    }
};
*/
// @lc code=end

