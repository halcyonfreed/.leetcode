/*
 * @lc app=leetcode.cn id=24 lang=cpp
 *
 * [24] 两两交换链表中的节点
 */

// @lc code=start
/**
 * Definition for singly-linked list. 需要自己额外定义的 天然自带递归
 * struct ListNode {
 *     int val;
 *     ListNode *next; //指针next
 *      下面是例子
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapPairs(ListNode* head){
        // 传入 head指针
        if (head==nullptr || head->next==nullptr){
            return head;
        }

        ListNode* subHead=swapPairs(head->next->next); // 套娃传入下下个，就是新的头

        //更新新的头
        ListNode* headNext=head->next;
        headNext->next=head;
        head->next=subHead;
        return headNext;
    }
};

/*
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {

        // 寻找递归终止条件
        // 1、head 指向的结点为 null 
        // 2、head 指向的结点的下一个结点为 null 
        // 在这两种情况下，一个节点或者空节点无论怎么交换操作，都是原来的 head
       if( head == NULL || head->next == NULL) {
          return head;
       }
  
        // 不断的通过递归调用，直到无法递归下去，递归的最小粒度是在最后一个节点或者最后两个节点
      ListNode *subHead = swapPairs(head->next->next);

        // 创建新的head，
        // 对于 head 这个节点来说，它是和它相邻的右边这个节点进行交换操作
        // 所以先要保存这个节点，并且经过上述递归终止条件的判断，head->next 是必然存在的
        ListNode *headNext = head->next;

        // head 原来是指向 headNext
        // 交换之后
        // headNext 指向 head
      headNext->next = head;
  
        // headNext 原来是指向 subHead
        // 现在需要让 head 指向 subHead
      head->next = subHead;
  
        // 交换之后，原来的第二位的那个节点 headNext 变成了第一位
        // 把它返回就行 新的头
      return headNext;  
        
    }
};
*/
// @lc code=end

