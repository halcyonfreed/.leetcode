/*
 * @lc app=leetcode.cn id=23 lang=cpp
 *
 * [23] 合并 K 个升序链表
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
    ListNode* mergeKLists(vector<ListNode*>& lists) {

    }
};


/*
// 登录 AlgoMooc 官网获取更多算法图解
// https://www.algomooc.com
// 作者：程序员吴师兄
// 微信：278166530
// 代码有看不懂的地方一定要私聊咨询吴师兄呀
// 合并K个升序链表（LeetCode 23）（优先队列做法）:https://leetcode.cn/problems/merge-k-sorted-lists/
class Solution {
public:
    struct Status {
        int val;
        ListNode ptr;
        bool operator < (const Status &rhs) const {
            return val > rhs.val;
        }
    };

    // 队列是遵循先进先出（First-In-First-Out）模式的，但有时需要在队列中基于优先级处理对象。
    // PriorityQueue 和队列 Queue 的区别在于 ，它的出队顺序与元素的优先级有关
    // 对 PriorityQueue 调用 remove() 或 poll() 方法 ，返回的总是优先级最高的元素
    priority_queue <Status> pq;

    ListNode mergeKLists(vector<ListNode*>& lists) {

        
        // 遍历所有链表
        for (auto node: lists) {
            // 把所有链表都加入到优先队列当中
            // 优先队列会自己处理，把头节点最小的值放到前面去
            if (node) pq.push({node->val, node});
        }


        // 添加一个虚拟头节点（哨兵），帮助简化边界情况的判断
      

        // 合并成功之后的尾节点位置
        ListNode dummyHead, *tail = &dummyHead;

        // 遍历优先队列，取出最下值出来
        while (!pq.empty()) {

            // 取出优先队列，即二叉堆的头节点，最小的节点
            auto f = pq.top(); pq.pop();

            // 把这个节点连接到合并链表的尾部
            tail->next = f.ptr; 

            // tail 的位置也随之发生变化
            tail = tail->next;

            // PriorityQueue 实现了 Queue 接口，不允许放入 null 元素
            if (f.ptr->next) pq.push({f.ptr->next->val, f.ptr->next});
        }

        // 整个过程其实就是「多路归并」过程
        // 返回结果
        return dummyHead.next;
    }
};
*/
// @lc code=end

