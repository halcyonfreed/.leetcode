#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(-1)
        dummy.next=head
        cur=dummy

        while cur.next and cur.next.next:
            if cur.next.val==cur.next.next.val:
                value=cur.next.val
                while cur.next and cur.next.val==value:
                    cur.next=cur.next.next
            else:
                cur=cur.next
        return dummy.next
'''
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 一开始设置一个虚拟节点，它的值为 -1，它的值可以设置为任何的数，因为我们根本不需要使用它的值
        dummy = ListNode(-1)

        # 将虚拟头节点和原链表头节点连接起来
        # 添加虚拟头节点之后，原链表的每个节点的地位都是一样的 防止删的是头节点时，原链表就不见了！
        dummy.next = head

        # 从虚拟头节点位置开始访问
        cur = dummy

        # 只要当前访问节点的下一个节点与下下个节点都存在，就继续访问下去
        while cur.next and cur.next.next :

            # 在访问过程中，会出现两种情况
            # 1、下一个节点与下下个节点相同，那么说明与这个节点值相同的所有节点都应该被删除掉
            if cur.next.val == cur.next.next.val : 

                # 删除的方法是先记录这个值，因为都被删了，所以前面的这个值要记录
                value = cur.next.val

                # 利用 while 循环，不断的查找出后面所有那些相同的节点值来
                while cur.next  and cur.next.val == value :

                    # 每次找到了一个相同的值，那么当前访问的节点 cur 就越过这个节点
                    cur.next = cur.next.next
                
            
            # 2、下一个节点与下下个节点不相同，说明 cur 可以加入到最终的结果链表中
            else:

                # 那么继续访问后面的节点
                cur = cur.next
   

        # 最终返回虚拟头节点的下一个节点就行了
        return dummy.next
'''
# @lc code=end

