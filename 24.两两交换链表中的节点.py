#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self,head:ListNode)->ListNode:
        # dummyhead=ListNode(next=head)
        # cur=dummyhead

        # while cur.next and cur.next.next:
        #     tmp1=cur.next
        #     tmp2=cur.next.next.next

        #     cur.next=cur.next.next
        #     cur.next.next=tmp1
        #     tmp1.next=tmp2

        #     cur=cur.next.next
        # return dummyhead.next

        if head is None or head.next is None:
            return head
        pre=head
        cur=head.next
        next=head.next.next # 新的头，两个两个操作
        
        cur.next=pre
        pre.next=self.swapPairs(next)

        return cur # 新的头



'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy_head = ListNode(next=head)
        current = dummy_head
        
        # 必须有cur的下一个和下下个才能交换，否则说明已经交换结束了
        while current.next and current.next.next:
            temp = current.next # 防止节点修改
            temp1 = current.next.next.next
            
            current.next = current.next.next
            current.next.next = temp
            temp.next = temp1
            current = current.next.next
        return dummy_head.next

        

'''
'''
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        # 寻找递归终止条件
        # 1、head 指向的结点为 null 
        # 2、head 指向的结点的下一个结点为 null 
        # 在这两种情况下，一个节点或者空节点无论怎么交换操作，都是原来的 head
        if head == None or head.next == None :
            return head

        # 不断的通过递归调用，直到无法递归下去，递归的最小粒度是在最后一个节点或者最后两个节点
        subHead = self.swapPairs(head.next.next)

        # 对于 head 这个节点来说，它是和它相邻的右边这个节点进行交换操作
        # 所以先要保存这个节点，并且经过上述递归终止条件的判断，head.next 是必然存在的
        headNext = head.next

        # head 原来是指向 headNext
        # 交换之后
        # headNext 指向 head
        headNext.next = head
  
        # headNext 原来是指向 subHead
        # 现在需要让 head 指向 subHead
        head.next = subHead
  
        # 交换之后，原来的第二位的那个节点 headNext 变成了第一位
        # 把它返回就行
        return headNext
'''
# @lc code=end

