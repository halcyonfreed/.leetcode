#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # if headA==None or headB==None:
        #     return None
        # pointA,pointB=headA,headB
        # while pointA!=pointB:
        #     if pointA==None:
        #         pointA=headB
        #     else:
        #         pointA=pointA.next
        #     if pointB == None:
        #         # 指针 pointA 跳转到链表 B 上  
        #         pointB = headA
        #     else:
        #         # 否则的话 pointB 不断的向后移动
        #         pointB = pointB.next
        # return pointA
        lenA=lenB=0
        cur=headA
        while cur:
            cur=cur.next
            lenA+=1
        
        cur=headB
        while cur:
            cur=cur.next
            lenB+=1
        
        curA,curB=headA,headB
        # 要让lenA>lenB
        if lenB>lenA:
            curA,curB=curB,curA
            lenA,lenB=lenB,lenA
        for _ in range(lenA-lenB):
            curA=curA.next
        
        while curB:
            if curA==curB:
                return curA
            else:
                curA=curA.next
                curB=curB.next
        return None

'''
没懂！！这题

（版本一）求长度，同时出发

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA, lenB = 0, 0
        cur = headA
        while cur:         # 求链表A的长度
            cur = cur.next 
            lenA += 1
        cur = headB 
        while cur:         # 求链表B的长度
            cur = cur.next 
            lenB += 1
        curA, curB = headA, headB
        if lenA > lenB:     # 让curB为最长链表的头，lenB为其长度
            curA, curB = curB, curA
            lenA, lenB = lenB, lenA 
        for _ in range(lenB - lenA):  # 让curA和curB在同一起点上（末尾位置对齐）
            curB = curB.next                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        while curA:         #  遍历curA 和 curB，遇到相同则直接返回
            if curA == curB:
                return curA
            else:
                curA = curA.next 
                curB = curB.next
        return None 

'''



'''
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        # 边界判断
        if( headA == None or headB == None ): 
            return None

        # 设置一个指针 pointA，指向链表 A 的头节点 因为headA本身不能动 所以用pointA
        pointA = headA

        # 设置一个指针 pointB，指向链表 B 的头节点
        pointB = headB

        # 指针 pointA 和 指针 pointB 不断向后遍历，直到找到相交点
        # 不用担心会跳不出这个循环，实际上在链表 headA 长度和链表 headB 长度的之和减一
        # pointA 和 pointB 都会同时指向 null
        # 比如 headA 的长度是 7，headB 的长度是 11，这两个链表不相交
        # 那么 pointA 移动了 7 + 11 - 1 次之后，会指向 null
        # pointB 移动了 7 + 11 - 1  次之后，也指向 null
        # 这个时候就跳出了循环
        while pointA != pointB:
            # 指针 pointA 一开始在链表 A 上遍历，当走到链表 A 的尾部即 null 时，跳转到链表 B 上 
            if pointA == None:
                # 指针 pointA 跳转到链表 B 上  
                pointA = headB
            else:
                # 否则的话 pointA 不断的向后移动
                pointA = pointA.next
            # 指针 pointB 一开始在链表 B 上遍历，当走到链表 B 的尾部即 null 时，跳转到链表 A 上 
            if pointB == None:
                # 指针 pointA 跳转到链表 B 上  
                pointB = headA
            else:
                # 否则的话 pointB 不断的向后移动
                pointB = pointB.next
        
        # 1、此时，pointA 和 pointB 指向那个相交的节点，返回任意一个均可
        # 2、此时，headA 和 headB 不相交，那么 pointA 和 pointB 均为 null，也返回任意一个均可
        return pointA
'''
# @lc code=end

