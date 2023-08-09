/*
 * @lc app=leetcode.cn id=496 lang=cpp
 *
 * [496] 下一个更大元素 I
 */

// @lc code=start
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {

    }
};

/*
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        // 使用 unordered_map 存储 nums2 中每个元素右边的第一个更大的值
        // 键为 nums2 中的元素，值为这个元素右边的第一个更大的值
        unordered_map<int, int> res;

        // 使用一个单调递增栈
        stack<int> stack;

        // 从后向前访问 nums2 中的元素
        for (int i = nums2.size() - 1; i >= 0; i--) {
            int num = nums2[i];

            // 在访问过程中维护单调递增栈的性质
            // 不断比较栈顶元素和当前元素 num
            // 1、直到找到一个比 num 更大的元素为止
            // 2、或者栈为空
            while (!stack.empty() && num >= stack.top()) {
                // 出栈操作
                stack.pop();
            }

            // 1、如果栈不为空，栈顶元素就是比 num 更大的元素
            // 存放栈顶元素的值到哈希集合 res 中
            // 2、如果栈为空，说明在 num 的右侧没有任何一个元素比它更大
            // 存放 -1 到哈希集合 res 中
            res[num] = stack.empty() ? -1 : stack.top();

            // 将当前元素入栈
            stack.push(num);
        }

        // 初始化结果数组
        vector<int> ans(nums1.size());

        // 由于两个数组都是没有重复元素的数组
        // nums1 是 nums2 的子集
        for (int i = 0; i < nums1.size(); i++) {
            // 从哈希集合 res 中找出对应元素的值
            ans[i] = res[nums1[i]];
        }

        // 返回结果
        return ans;
    }
};
*/
// @lc code=end

