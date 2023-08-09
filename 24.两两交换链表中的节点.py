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
        if head==None or head.next==None:
            return head
        subHead=self.swapPairs(head.next.next) # recursion递归，套娃

        headNext=head.next
        headNext.next=head
        head.next=subHead
        return headNext

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

