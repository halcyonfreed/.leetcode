/*
 * @lc app=leetcode.cn id=82 lang=cpp
 *
 * [82] 删除排序链表中的重复元素 II
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode *dummy=new ListNode(-1);
        dummy->next=head;
        ListNode *cur=dummy;

        while(cur->next!=nullptr && cur->next->next!=nullptr){
            if (cur->next->val==cur->next->next->val){
                int value=cur->next->val;
                while(cur->next && cur->next->val==value){
                    cur->next=cur->next->next;
                }
            }
            else{
                cur=cur->next;
            }
        }
        return dummy->next;

    }
};
/*

// 登录 AlgoMooc 官网获取更多算法图解
// https://www.algomooc.com
// 作者：程序员吴师兄
// 代码有看不懂的地方一定要私聊咨询吴师兄呀
// https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/submissions/
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        // 一开始设置一个虚拟节点，它的值为 -1，它的值可以设置为任何的数，因为我们根本不需要使用它的值
        ListNode *dummy = new ListNode(-1);

        // 将虚拟头节点和原链表头节点连接起来
        // 添加虚拟头节点之后，原链表的每个节点的地位都是一样的
        dummy->next = head;

        // 从虚拟头节点位置开始访问
        ListNode *cur = dummy;

        // 只要当前访问节点的下一个节点与下下个节点都存在，就继续访问下去
        while (cur->next != NULL && cur->next->next != NULL) {

            // 在访问过程中，会出现两种情况
            // 1、下一个节点与下下个节点相同，那么说明与这个节点值相同的所有节点都应该被删除掉
            if (cur->next->val == cur->next->next->val) {

                // 删除的方法是先记录这个值
                int value = cur->next->val;

                // 利用 while 循环，不断的查找出那些相同的节点值来
                while (cur->next != NULL && cur->next->val == value) {

                    // 每次找到了一个相同的值，那么当前访问的节点 cur 就越过这个节点
                    cur->next = cur->next->next;
                }
            
            // 2、下一个节点与下下个节点不相同，说明 cur 可以加入到最终的结果链表中
            } else {

                // 那么继续访问后面的节点
                cur = cur->next;
            }
        }

        // 最终返回虚拟头节点的下一个节点就行了
        return dummy->next;

    }
};
*/
// @lc code=end

