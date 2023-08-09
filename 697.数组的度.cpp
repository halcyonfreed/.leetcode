/*
 * @lc app=leetcode.cn id=697 lang=cpp
 *
 * [697] 数组的度
 */

// @lc code=start
class Solution {
public:
    int findShortestSubArray(vector<int>& nums) {
        unordered_map<int, vector<int>> mp;
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            if (mp.count(nums[i])) {
                mp[nums[i]][0]++;
                mp[nums[i]][2] = i;
            } else {
                mp[nums[i]] = {1, i, i};
            }
        }
        int maxNum = 0, minLen = 0;
        for (auto& [_, vec] : mp) {
            if (maxNum < vec[0]) {
                maxNum = vec[0];
                minLen = vec[2] - vec[1] + 1;
            } else if (maxNum == vec[0]) {
                if (minLen > vec[2] - vec[1] + 1) {
                    minLen = vec[2] - vec[1] + 1;
                }
            }
        }
        return minLen;
    }
};
/*
// 登录 AlgoMooc 官网获取更多算法图解
// https://www.algomooc.com
// 作者：程序员吴师兄
// 微信：wzb_3377
// 代码有看不懂的地方一定要私聊咨询吴师兄呀
// 数组的度（LeetCode 697）：https://leetcode.cn/problems/degree-of-an-array/submissions/
class Solution {
    public int findShortestSubArray(int[] nums) {

        // 1、key 为数组中的值
        // 2、value 为一个数组
        // 2.1 数组的第一个元素为 key 出现的次数
        // 2.2 数组的第二个元素为 key 第一次出现的位置
        // 2.3 数组的第三个元素为 key 最后一次出现的位置
        Map<Integer,int[]> map = new HashMap<Integer,int[]>();

        // 遍历数组，统计每个元素出现的次数、第一次出现的位置、最后一次出现的位置
        // 把结果更新到 map 中
        for( int i = 0 ;i < nums.length ; i++ ){

            // 如果哈希表 map 中已经存在当前这个元素的 key
            // 说明在遇到 nums[i] 之前已经遇到了 nums[i] 这个值
            if(map.containsKey(nums[i])){

                // 更新这个元素出现的次数
                map.get(nums[i])[0]++;

                // 更新这个元素最后一次出现的位置
                map.get(nums[i])[2] = i;

            // 如果哈希表 map 中没有存在当前这个元素的 key
            // 说明现在是第一次遇到 nums[i] 这个值
            }else{
                
                // 更新这个元素出现的次数为 1
                // 更新这个元素第一次出现的位置为 i
                // 更新这个元素最后一次出现的位置为 i
                map.put(nums[i],new int[]{1,i,i});
            }
        }

        // 记录元素出现的最多次数
        int maxNum = 0;

        // 记录符合要求的元素并且前后位置差最小的数的长度
        int minLen = 0;

        // 遍历哈希表 map ，找到元素出现次数最多，且前后位置差最小的数
        for(Map.Entry<Integer, int[]> entry : map.entrySet()){

            // 获取当前元素里面的数组
            int[] temp = entry.getValue();

            // temp[0] 为 key 出现的次数
            // 如果这个值比 maxNum 更大，那么数字需要更新
            if(temp[0] > maxNum){

                // 更新元素出现的最多次数
                maxNum = temp[0];

                // 记录符合要求的元素并且前后位置差最小的数的长度
                minLen = temp[2] - temp[1] + 1 ;

            // 如果这个值和 maxNum 相同，那么 minLen 需要更新
            }else if(temp[0] == maxNum){
                // 对比 minLen 和当前这个元素的前后位置差
                if( minLen > temp[2]- temp[1] + 1 ){
                    // 取较小值
                    minLen = temp[2] - temp[1] + 1;
                }
            }
        }
        // 返回结果
        return minLen;
    }
}
*/
// @lc code=end

