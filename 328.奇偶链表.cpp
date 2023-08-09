/*
 * @lc app=leetcode.cn id=328 lang=cpp
 *
 * [328] 奇偶链表
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
    ListNode* oddEvenList(ListNode* head) {
        if (head==nullptr || head->next==nullptr) return head;
        ListNode* odd=head;
        ListNode* even=head->next;
        ListNode* evenHead=even;

        while (even!=nullptr && even->next!=nullptr){
            odd->next=even->next;
            odd=odd->next;

            even->next=odd->next;
            even=even->next;
        }
        odd->next=evenHead;
        return head;
    }
};
/*
// 登录 AlgoMooc 官网获取更多算法图解
// https://www.algomooc.com
// 作者：程序员吴师兄
// 代码有看不懂的地方一定要私聊咨询吴师兄呀
// 奇偶链表（ LeetCode 328 ）:https://leetcode-cn.com/problems/odd-even-linked-list/
class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        // 边界情况处理，如果链表为空或者只有一个节点，返回 head 就行
        if(head == NULL || head->next == NULL ) return head;

        // 设置一个指针，指向链表的头节点，odd 代表奇数节点的头节点
        ListNode* odd = head;

        // 设置一个指针，指向链表的头节点的下一个节点，even 代表偶数节点的头节点
        ListNode* even = head->next; 

        // 设置一个指针，指向偶数节点的头节点，最终让奇数节点的尾节点的 next 指针指向它，妙啊，
        ListNode* evenHead = even;
        
        // 从偶数链表的头节点开始向后遍历
        // 如果当前节点为空，或者后一节点为空，那么说明整个链表已经查看完毕，不需要再遍历了
        //even在odd后面，所以用even判结束？
        while(even != NULL && even->next != NULL){
            // 原先奇数节点的下一个节点是偶数节点，即 even 这个节点
            // 根据数学知识，奇数后面一定是偶数，偶数后面一定是奇数
            // 那么 even->next 节点必然是奇数节点
            // 所以让 odd 这个奇数节点的 next 指针指向 even->next 这个奇数节点
            // 这样，odd 上面都是奇数 先换odd，再换even
            odd->next = even->next;
            // 让 odd 移动到最新的由奇数节点组成的链表的尾部位置
            odd = odd->next;

            // 这个时候，odd->next 必然是偶数节点
            // 所以让 even 这个偶数节点的 next 指针指向 odd->next 这个偶数节点
            even->next = odd->next;
            // 让 even 移动到最新的由偶数节点组成的链表的尾部位置
            even = even->next;
        }

        // 此时，原链表所有的节点已经遍历完毕
        // odd 上都是奇数节点
        // even 都是偶数节点
        // 根据题目要求，奇数节点都在偶数节点之前
        // 所以让此时右奇数节点组成的链表的尾部的 next 指针指向由偶数节点组成的链表的头部
        odd->next = evenHead;

        // 最后返回原链表的头部节点就可以了
        // 链表的头部节点没有发生过变化，因为它是奇数节点，并且是第一个奇数节点
        return head;
    }
};
*/
// @lc code=end

