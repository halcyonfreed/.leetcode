#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # # 可以直接自己默出来
        # dummyhead=ListNode(next=head)
        # slow=fast=dummyhead  #可以连等

        # for i in range(n+1):
        #     fast=fast.next
        # while fast:
        #     slow=slow.next
        #     fast=fast.next
        
        # # 删除
        # slow.next=slow.next.next

        # return dummyhead.next
        dummyhead=ListNode(next=head)
        slow=fast=dummyhead

        for i in range(n+1):
            fast=fast.next
        while fast:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return dummyhead.next


'''
# 本题文字版详解请访问下方网站
# https://www.algomooc.com
# 作者：程序员吴师兄
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 添加表头
        dummy = ListNode(-1)
        dummy.next = head

        # 寻找需要删除的节点节点
        cur = head

        # 指针 latter 指向虚拟头结点
        latter = dummy

        former = head

        # 让 former 指针先向前走 n 步 它先探路
        for i in range(n):
            # former 指针向后移动
            former = former.next

        # 接下来，让这两个指针 former 和 latter 同时向前移动，直到前指针 former 指向 NULL
        while former is not None:
            # former 指针向后移动
            former = former.next

            # latter 来到 cur 的位置
            latter = cur

            # cur 指针向后移动
            cur = cur.next

        # 删除 cur 这个位置的结点
        latter.next = cur.next

        # 返回虚拟头结点的下一个结点
        return dummy.next
'''
# @lc code=end

