#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur=head
        # while cur.next and cur: cur cur.next顺序变了就不行！
        while cur and cur.next:
            if cur.val==cur.next.val:
                cur.next=cur.next.next
            else:
                cur=cur.next
        return head
'''
# 登录 AlgoMooc 官网获取更多算法图解
# https://www.algomooc.com
# 作者：程序员吴师兄
# 代码有看不懂的地方一定要私聊咨询吴师兄呀
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 从链表的头节点开始访问每一个节点
        cur = head

        # 在访问过程中，只要当前节点和当前节点的下一个节点有值，就不断访问下去
        while cur and cur.next :

            # 当前节点和当前节点的下一个节点有两种关系

            # 1、当前节点和当前节点的下一个节点相同，此时要删除重复元素
            # 由于链表已经是排序的，所以去重操作只需要跳过后面这个重复的节点就行
            if cur.val == cur.next.val :

                # 执行这个操作之后，cur.next 被跳过去了
                cur.next = cur.next.next

            # 2、当前节点和当前节点的下一个节点不相同，那么 cur 这个节点可以保留下来，继续访问后面的节点
            else:
                # 继续访问后面的节点
                cur = cur.next

        # 返回链表的头节点就是结果
        return head
'''
# @lc code=end

