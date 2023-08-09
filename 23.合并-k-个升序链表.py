#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并 K 个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0: 
            # 空
            return None
        import heapq
        heap=[]

        for node in lists:
            while node:
                heapq.heappush(heap,node.val)
                node=node.next

        dummy=ListNode(None)
        tail=dummy #???
        while heap:
            temp_node=ListNode(heappop(heap))
            tail.next=temp_node
            tail=temp_node
        return dummy.next

'''

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists or len(lists) == 0:
            return None
        import heapq
        heap = []
        # 和 Java有所不同，是将所有元素都取出放入堆中
        for node in lists:
            while node:
                heapq.heappush(heap, node.val)
                node = node.next
        # 添加一个虚拟头节点（哨兵），帮助简化边界情况的判断 
        dummy = ListNode(None)
        # 合并成功之后的尾节点位置
        tail = dummy
        # 依次将堆中的元素取出(因为是小顶堆，所以每次出来的都是目前堆中值最小的元素），然后重新构建一个列表返回
        while heap:
            temp_node = ListNode(heappop(heap))
            tail.next = temp_node
            tail = temp_node
        return dummy.next
'''
# @lc code=end

