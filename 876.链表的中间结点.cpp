/*
 * @lc app=leetcode.cn id=876 lang=cpp
 *
 * [876] 链表的中间结点
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
    ListNode* middleNode(ListNode* head) {
        ListNode* slow=head;
        ListNode* fast=head;

        while(fast && fast->next){
            slow=slow->next;
            fast=fast->next->next;
        }
        return slow;
    }
};

/*
class Solution {
public:
    ListNode* middleNode(ListNode* head) {

        // 设置两个指针，一开始都指向链表的头节点
        ListNode* slow = head;

        ListNode* fast = head;

        // 接下来，让这两个指针向前移动
        // 如果可以移动，那么就会让快指针每次移动两步，慢指针每次移动一步
        // 而快指针可以移动两步的前提就是当前节点不为空，同时下一节点也不为空
        // 这样才能保证 fast.next 有值、fast.next.next 有值
        while(fast != NULL && fast->next != NULL){

            // 慢指针每次移动一步
            slow = slow->next;

            // 快指针每次移动两步
            fast = fast->next->next;
        }

        // 最后，slow 指向的就是中间节点
        return slow;

    }
};
*/
// @lc code=end

