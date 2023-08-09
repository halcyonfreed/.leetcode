/*
 * @lc app=leetcode.cn id=92 lang=cpp
 *
 * [92] 反转链表 II
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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        ListNode* dummy=new ListNode(-1);
        dummy->next=head;

        ListNode* pre=dummy;
        ListNode* cur=head;

        for (int i=0;i<left-1;++i){
            pre=pre->next;
            cur=cur->next; 
        }

        for(int i=0;i<right-left;++i){
            ListNode* temp=cur->next;
            cur->next=temp->next;
            temp->next=pre->next;
            pre->next=temp; 
            
            // cur->next = temp->next
            // temp->next = pre->next;
            // pre->next = temp;
        }
        return dummy->next;
    }
};

/*
// 登录 AlgoMooc 官网获取更多算法图解
// https://www.algomooc.com
// 作者：程序员吴师兄
// 代码有看不懂的地方一定要私聊咨询吴师兄呀
// 反转链表 II （ LeetCode 92 ）：https://leetcode-cn.com/problems/reverse-linked-list-ii
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        // 一开始设置一个虚拟节点，它的值为 -1，它的值可以设置为任何的数，因为我们根本不需要使用它的值
        // 设置虚拟节点的目的是为了让原链表中所有节点就都可以按照统一的方式进行翻转
        // 比如如果翻转的区间包含了原链表中的第一个位置，那么如果不设置 dummy
        // 在翻转的过程中需要设置其它的临时变量来保持第一位置节点的指针
        // 具体可以通过动画来理解
        ListNode *dummy = new ListNode(-1);

        // 让虚拟节点指向原链表的头部
        dummy->next = head;
        
        // 设置一个指针，指向以虚拟头节点为链表的头部位置
        ListNode *pre = dummy;

        // 设置一个指针，指向原链表的头部位置
        ListNode *cur = head;


        // 从虚拟头节点出发，pre 走 left - 1 步找到需要翻转的左区间;同步走
        // for 循环结束后，pre 的右节点是需要翻转的节点
        // for 循环结束后，cur 指向的就是需要翻转的节点
        for (int i = 0; i < left - 1; i++) {
           
            // pre 不断的向右移动，直到走到翻转的左区间为止
            pre = pre->next;
            // cur 不断的向右移动，找到了需要翻转的第一个节点
            cur = cur->next;
        }

        // 开始翻转这些节点
        for (int i = 0; i < right - left; i++) {
            
            // 设置临时变量，保存当前需要翻转节点的后面的节点
            ListNode *temp = cur->next;

            // 这个时候，让 temp 和 cur 两个节点翻转一下
            // 比如，一开始 i = 0 的时候 cur 为 2， temp 为 3, pre=1
            // 执行完下面的代码，如果原链表是
            // 1 --> 2 --> 3 --> 4 --> 5
            // 断pre->next, cur->next, tmp->next
            // 1 --> 3 --> 2 --> 4 --> 5
            
            // cur 的下一节点是等号右侧的值
            // i = 0 的时候， cur 为 2，cur->next->next 的值是 4
            // 所以，这行代码让 cur 的下一节点不是 3 ，而是 4 
            // 2 --> 4
            // 等价于 cur->next = temp->next
            // 这个断的顺序 很微妙，搞不清楚
            cur->next = cur->next->next;

            // temp 的下一节点是等号右侧的值
            // i = 0 的时候， temp 为 3，pre 为 1，pre 下一节点的值是 2
            // 所以，这行代码让 temp 的下一节点不是 4 ，而是 2 
            // 3 --> 2 pre->next不是cur
            temp->next = pre->next;

            // pre 的下一节点是等号右侧的值
            // i = 0 的时候， pre 为 1，temp 的值是 3
            // 所以，这行代码让 pre 的下一节点为 3
            // 1 --> 3
            pre->next = temp; //这个顺序不能改，会有问题

            // i = 0 结束之后，链表变成了
            // 1 --> 3 --> 2 --> 4 --> 5
           
        }

        // 最后返回虚拟头节点的下一个节点，因为虚拟节点不在链表中
        return dummy->next;
    }
};
*/
// @lc code=end

