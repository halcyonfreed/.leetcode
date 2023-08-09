/*
 * @lc app=leetcode.cn id=125 lang=cpp
 *
 * [125] 验证回文串
 */

// @lc code=start
class Solution {
public:
    bool isPalindrome(string s) {
        int left=0,right=s.size()-1;
        while(left<right){
            //  isalnum() 方法检测字符串是否由字母和数字组成
            while(left < right && !isalnum(s[left])) left++;
            while(left < right && !isalnum(s[right])) right--;
        
        if (left<right){
            // 大写字母则将该对应的小写字母返回tolower()
            if (tolower(s[left])!=tolower(s[right])){
                return false;
            }
            left++;
            right--;
        }
        }
        return true;
    }
};


/*
class Solution {
public:
    bool isPalindrome(string s) {
        // 设置左右两个指针
        int left = 0 ;
        
        int right = s.size() - 1 ;


        // 移动和观察者两个指针所指向元素之间的关系
        while (left < right) {
            
            // 这里的逻辑有点像快速排序的代码

            // 如果 left 指向的元素不是字母、也不是数字
            // 那么可以忽略掉这个元素，即让 left 向右移动
            while (left < right && !isalnum(s[left])) {
                // left 向右移动
                left++;

            }

            // 如果 right 指向的元素不是字母、也不是数字
            // 那么可以忽略掉这个元素，即让 right 向左移动
            while (left < right && !isalnum(s[right])) {
                // right 向左移动
                right--;

            }

            // 来到这里时
            // 要么 left 和 right 相遇了，跳出循环
            // 要么 left 和 right 还没有相遇，并且它们都是指向字母或者数字
            if (left < right) {

                // 只需要判断一下 left 和 right 指向的元素值是否相同就行
                // 题目说明 可以忽略字母的大小写
                if (tolower(s[left]) != tolower(s[right])) {
                    // 不相同就直接说明不是回文串
                    return false;
                }

                // 否则，继续让两个指针向内移动

                // left 向右移动
                left++;

                // right 向左移动
                right--;
            }
        }

        // 最后，没有得到 false 的答案就说明是回文串，返回 true
        return true;

    }
};
*/
// @lc code=end

