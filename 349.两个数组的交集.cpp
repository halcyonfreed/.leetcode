/*
 * @lc app=leetcode.cn id=349 lang=cpp
 *
 * [349] 两个数组的交集
 */

// @lc code=start
class Solution {
public:
    vector<int> intersection(vector<int>& nums1,vector<int>& nums2){
        sort(nums1.begin(),nums1.end());
        sort(nums2.begin(),nums2.end());

        int length1=nums1.size(),length2=nums2.size();
        vector<int> res;
        int index=0,index1=0,index2=0;

        while(index1<length1 && index2<length2){
            int num1=nums1[index1],num2=nums2[index2];
            if(num1==num2){
                if(!res.size() || num1!=res.back()){
                    res.push_back(num1);
                }
                index1++;
                index2++;
            }
            else if(num1<num2){
                index1++;
            }
            else {
                index2++;
            };
        }
        return res;
    }
};
/*
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {

        // 首先对两个数组进行排序
        sort(nums1.begin(), nums1.end());

        sort(nums2.begin(), nums2.end());
       

        // 计算出两个数组的长度
        int length1 = nums1.size();

        int length2 = nums2.size();
        
    
        // 两个数组的交集结果数组长度必然是小于等于最短数组的长度
        vector<int> res ;

        // 设置三个索引指针

        // index 指向结果数组 res ，每当 index 指向的位置填充了元素就向后移动
        // int index = 0;
        
        // index1 指向数组 nums1 中的元素，将该元素和 index2 指向数组 nums2 中的元素进行比较
        int index1 = 0;
        
        // index2 指向数组 nums2 中的元素，将该元素和 index1 指向数组 nums1 中的元素进行比较
        int index2 = 0;

        // 移动 index1 和 index2 
        while (index1 < length1 && index2 < length2) {
            
            // 获取 index1 指向的元素值
            int num1 = nums1[index1];
            
            // 获取 index2 指向的元素值
            int num2 = nums2[index2];

            // num1 和 num2 的大小关系有三种

            // 1、num1 == num2
            if (num1 == num2) {

                // 由于输出结果中的每个元素一定是 【唯一】 的，所以要做一下判断
                // 如果 res 中的 index 在起始位置，说明还没有存放元素
                // 那么这个相等的元素可以存放到 res 中

                // 如果 res 中的 index 不在起始位置
                // 当它前面存放的元素并不是现在想要存放的元素
                // 那么这个相等的元素可以存放到 res 中
                if ( !res.size() || num1 != res.back()) {

                    // 存放到 res 中
                    res.push_back(num1);
                   
                }

                // 移动 index1 ，比较其它元素
                index1++;
               
                // 移动 index2 ，比较其它元素
                index2++;

            // 2、num1 < num2
            } else if (num1 < num2) {
                
                // 由于两个数组已经排序了，说明此时 num1 肯定会小于 nums2 数组中 num2 后面所有的数
                // 那 num1 肯定是无法在 nums2 中找到相等的元素
                // 移动 index1 ，比较其它元素
                index1++;

            // 3、num1 > num2
            } else {

                // 由于两个数组已经排序了，说明此时 num2 肯定会小于 nums1 数组中 num1 后面所有的数
                // 那 num2 肯定是无法在 nums1 中找到相等的元素
                // 移动 index2 ，比较其它元素
                index2++;

            }
        }

        // 最后返回结果数组中有值的那些元素就行
        return res;

    }
};
*/
// @lc code=end

