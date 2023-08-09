/*
 * @lc app=leetcode.cn id=160 lang=cpp
 *
 * [160] 相交链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if (headA==nullptr ||headB==nullptr) return nullptr;
        ListNode *pointA=headA,*pointB=headB;
        while(pointA!=pointB){
        // while(*pointA!=*pointB){ 比内存地址，而不是比指针内容 因为*pointA是内容 即headA结构体，结构体直接不能直接比较有问题的https://blog.csdn.net/Chz_1/article/details/109086388
            if (pointA==nullptr) pointA=headB;
            else pointA=pointA->next;
            if (pointB==nullptr) pointB=headA;
            else pointB=pointB->next;
        }
        return pointA;
    }
};

/*
规律
也就是说，无论 A、B 两个链表是否有相交点，最终都会指向一个相同的节点，要么是它们的公共尾部，要么是 NULL。
让指针 pointA 和 pointB 分别指向链表 A 和链表 B 的头结点，之后两个指针分别以步幅为 1 的速度向链表的尾部遍历。
当指针 pointA 遍历到链表 A 的尾节点时，此时指针 pointA 走了 a 个节点，将指针 pointA 指向链表 B 的头部，继续向后遍历，直至走到 c1，此时指针 pointA 总共走了 a + ( b - c ) 步。
当指针 pointB 遍历到链表 B 的尾节点时，此时指针 pointB 走了 b 个节点，将指针 pointB 指向链表 A 的头部，继续向后遍历，直至走到 c1，此时指针 pointB 总共走了 b + ( a - c ) 步。
根据数学知识，a + ( b - c ) = b + ( a - c )   ，如果 c > 0，表明两链表有公共尾部， c1 存在，两两链表同时到达 c1；如果 c = 0，表明两链表没有公共尾部，指针 pointA 和 pointB 都指向 NULL。

// 登录 AlgoMooc 官网获取更多算法图解
// https://www.algomooc.com
// 作者：程序员吴师兄
// 代码有看不懂的地方一定要私聊咨询吴师兄呀
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        // 边界判断
        if (headA == NULL || headB == NULL) return NULL;
        
        // 设置一个指针 pointA，指向链表 A 的头节点 *pointA是pointA指向的值，pointA是指针本身
        ListNode *pointA = headA;
        
        // 设置一个指针 pointB，指向链表 B 的头节点
        ListNode *pointB = headB;

        // 指针 pointA 和 指针 pointB 不断向后遍历，直到找到相交点
        // 不用担心会跳不出这个循环，实际上在链表 headA 长度和链表 headB 长度的之和减一
        // pointA 和 pointB 都会同时指向 null
        // 比如 headA 的长度是 7，headB 的长度是 11，这两个链表不相交
        // 那么 pointA 移动了 7 + 11 - 1 次之后，会指向 null
        // pointB 移动了 7 + 11 - 1  次之后，也指向 null
        // 这个时候就跳出了循环
        while (pointA != pointB) {
            // 指针 pointA 一开始在链表 A 上遍历，当走到链表 A 的尾部即 null 时，跳转到链表 B 上 
            if( pointA == NULL){
                // 指针 pointA 跳转到链表 B 上  
                pointA = headB;
            }else{
                // 否则的话 pointA 不断的向后移动
                pointA = pointA->next;
            }

             // 指针 pointB 一开始在链表 B 上遍历，当走到链表 B 的尾部即 null 时，跳转到链表 A 上 
            if( pointB == NULL){
                // 指针 pointA 跳转到链表 B 上  
                pointB = headA;
            }else{
                // 否则的话 pointB 不断的向后移动
                pointB = pointB->next;
            }
        }
        
        // 1、此时，pointA 和 pointB 指向那个相交的节点，返回任意一个均可
        // 2、此时，headA 和 headB 不相交，那么 pointA 和 pointB 均为 null，也返回任意一个均可
        return pointA;
    }
};
*/
// @lc code=end

