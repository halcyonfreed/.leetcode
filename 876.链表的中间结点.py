#
# @lc app=leetcode.cn id=876 lang=python3
#
# [876] 链表的中间结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow,fast=head,head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        return slow

'''
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # 设置两个指针，一开始都指向链表的头节点
        slow = head

        fast = head

        # 接下来，让这两个指针向前移动
        # 如果可以移动，那么就会让快指针每次移动两步，慢指针每次移动一步
        # 而快指针可以移动两步的前提就是当前节点不为空，同时下一节点也不为空
        # 这样才能保证 fast.next 有值、fast.next.next 有值
        while fast and fast.next :

            # 慢指针每次移动一步
            slow = slow.next

            # 快指针每次移动两步
            fast = fast.next.next
    

        # 最后，slow 指向的就是中间节点
        return slow
'''
# @lc code=end

