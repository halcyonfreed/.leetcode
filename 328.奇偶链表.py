#
# @lc app=leetcode.cn id=328 lang=python3
#
# [328] 奇偶链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head

        odd=head
        even,evenHead=head.next,head.next

        while even and even.next:
            odd.next=even.next
            odd=odd.next

            even.next=odd.next
            even=even.next

        odd.next=evenHead
        return head
'''

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # 边界情况处理，如果链表为空或者只有一个节点，返回 head 就行
        if head == None or head.next == None :
           return head

        # 设置一个指针，指向链表的头节点，odd 代表奇数节点的头节点
        odd = head

        # 设置一个指针，指向链表的头节点的下一个节点，even 代表偶数节点的头节点
        even = head.next 

        # 设置一个指针，指向偶数节点的头节点，最终让奇数节点的尾节点的 next 指针指向它
        evenHead = even
        
        # 从偶数链表的头节点开始向后遍历
        # 如果当前节点为空，或者后一节点为空，那么说明整个链表已经查看完毕，不需要再遍历了
        while even != None and even.next != None :
            # 原先奇数节点的下一个节点是偶数节点，即 even 这个节点
            # 根据数学知识，奇数后面一定是偶数，偶数后面一定是奇数
            # 那么 even.next 节点必然是奇数节点
            # 所以让 odd 这个奇数节点的 next 指针指向 even.next 这个奇数节点
            # 这样，odd 上面都是奇数
            odd.next = even.next
            # 让 odd 移动到最新的由奇数节点组成的链表的尾部位置
            odd = odd.next

            # 这个时候，odd.next 必然是偶数节点
            # 所以让 even 这个偶数节点的 next 指针指向 odd.next 这个偶数节点
            even.next = odd.next
            # 让 even 移动到最新的由偶数节点组成的链表的尾部位置
            even = even.next
        

        # 此时，原链表所有的节点已经遍历完毕
        # odd 上都是奇数节点
        # even 都是偶数节点
        # 根据题目要求，奇数节点都在偶数节点之前
        # 所以让此时右奇数节点组成的链表的尾部的 next 指针指向由偶数节点组成的链表的头部
        odd.next = evenHead

        # 最后返回原链表的头部节点就可以了
        # 链表的头部节点没有发生过变化，因为它是奇数节点，并且是第一个奇数节点
        return head
'''
# @lc code=end

