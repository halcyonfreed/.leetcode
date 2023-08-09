/*
 * @lc app=leetcode.cn id=19 lang=cpp
 *
 * [19] 删除链表的倒数第 N 个结点
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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummy=new ListNode(-1);
        dummy->next=head;

        ListNode* cur=head;
        ListNode* latter=dummy;
        ListNode* former=head;

        for (int i=0;i<n;++i){
            former=former->next;
        }
        while(former!=nullptr){
            former=former->next;
            latter=cur;
            cur=cur->next;
        }
        latter->next=cur->next; //删了cur
        return dummy->next;
    }
};
/*
// 本题文字版详解请访问下方网站
// https://www.algomooc.com
// 作者：程序员吴师兄 这是java版本的不对！！
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {

        // 添加表头
        ListNode dummy = new ListNode(-1);

        dummy.next = head;

        // 寻找需要删除的节点节点
        ListNode cur = head;

        // 指针 latter 指向虚拟头结点
        ListNode latter = dummy;

        ListNode former = head;

        // 让 former 指针先向前走 n 步
        for (int i = 0 ; i < n; i++) {
            // former 指针向后移动
            former = former.next;
        }

        // 接下来，让这两个指针 former 和 latter 同时向前移动，直到前指针 former 指向 NULL
        while (former != null) {
            // former 指针向后移动
            former = former.next;

            // latter 来到 cur 的位置
            latter = cur;

            // cur 指针向后移动
            cur = cur.next;
        }

        // 删除 cur 这个位置的结点
        latter.next = cur.next;

        // 返回虚拟头结点的下一个结点
        return dummy.next;
    }
}
*/
// @lc code=end

