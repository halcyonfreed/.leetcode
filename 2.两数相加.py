#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(-1)
        carryBit=0
        cur=dummy

        while l1 or l2:
            # 这种写法 我不一定会，没想到，天天写，坚持4年，不能间端，就像拉小提琴一样写到闭着眼睛也会 comprehension
            x=l1.val if l1 else 0
            y=l2.val if l2 else 0

            # 求和、进位、个位
            sum=x+y+carryBit
            carryBit=sum//10
            digit=sum%10

            digitNode=ListNode(digit) # 创建才有后面的 
            cur.next=digitNode
            cur=cur.next

            # l1=l1.next if l1
            # l1=l1.next if l1 else l1
            if l1 :
               l1 = l1.next
            if l2 :
               l2 = l2.next

        if carryBit==1:
            carryBitNode=ListNode(carryBit)
            cur.next=carryBitNode

        return dummy.next



'''
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 构建一个链表用来存放 l1 和 l2 两个链表相加的结果
        # 其中 dummy 这个节点为虚拟头结点
        # dummy = ListNode()
        dummy = ListNode(-1)

        # 设置一个进位，初始化为 0
        # 两个个位数相加，进位只能是 1 或者 0
        # 比如 7 + 8 = 15，进位是 1
        # 比如 2 + 3 = 6，没有进位，或者说进位是 0
        carryBit = 0

        # l1 和 l2 有可能为空，所以先默认结果链表从虚拟头结点位置开始
        cur = dummy

        # 同时遍历 l1 和 l2
        # 只要此时 l1 和 l2 两个链表中的任意链表中节点有值，就一直加下去
        # 直到两个链表中的所有节点都遍历完毕为止
        while l1 or l2 :
            # 获取 l1 链表中节点的值
            # 观察此时 l1 中的节点是否有值
            # 如果节点不存在，那么就用 0 来占位
            # 否则，将 l1 的节点值赋值给 x
            x = l1.val if l1 else 0

            # 获取 l2 链表中节点的值
            # 观察此时 l2 中的节点是否有值
            # 如果节点不存在，那么就用 0 来占位
            # 否则，将 l2 的节点值赋值给 y
            y = l2.val if l2 else 0
   
            # 每一位计算的同时需要考虑上一位的进位情况
            sum = x + y + carryBit
            
            # 获取当前计算结果的十位数
            # 比如 7 + 8 = 15
            # 那么 sum / 10 = 1，进位为 1
            carryBit = sum // 10

            # 获取当前计算结果的个位数
            # 比如 7 + 8 = 15
            # 那么 sum % 10 = 5
            digit = sum % 10

            # 构建一个节点用来存放这个个位数
            digitNode = ListNode(digit)

            # 把这个节点加入到结果链表中
            cur.next = digitNode

            # 移动 cur 的位置，观察后面应该存放什么节点
            cur = cur.next
            
            # l1 链表中还有节点未遍历完毕就继续遍历下去
            if l1 :
               l1 = l1.next

            # l2 链表中还有节点未遍历完毕就继续遍历下去
            if l2 :
               l2 = l2.next

        # 两个链表的尾节点相加之后，有可能产生进位的情况
        # 所以，需要构建一个新的节点用来存放这个进位的结果
        if carryBit == 1 :
            # 构建一个节点用来存放这个进位
            carryBitNode = ListNode(carryBit)

            # 把这个节点加入到结果链表中
            cur.next = carryBitNode

        # 最后返回结果链表的头节点就行，即虚拟头结点的下一个节点
        return dummy.next
'''
# @lc code=end

