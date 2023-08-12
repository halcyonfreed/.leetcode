#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k==0:
            # 如果空的
            return head 
        
        # 求链表的长度，没法直接求，用遍历
        _len=0 # _内部变量不可以改
        tempHead=head
        while tempHead:
            tempHead=tempHead.next
            _len+=1

        k=k%_len
        former,latter=head,head # 头和尾
        for i in range(k):
            former=former.next
        while former.next:
            former=former.next
            latter=latter.next
        former.next=head
        newHead=latter.next
        latter.next=None

        return newHead


'''
 class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 边界条件判断
        if not head or k == 0 :
            return head

        # 1、第一步先要计算出链表的长度来
        _len = 0

        # 2、这里我们设置一个指针指向链表的头节点的位置
        tempHead = head

        # 3、通过不断的移动 tempHead ，来获取链表的长度
        while tempHead :

            # tempHead 不断向后移动，直到为 NULL
            tempHead = tempHead.next

            # 每次遍历一个新的节点，意味着链表长度新增 1
            _len += 1

    

        # 由于题目中的 k 会超过链表的长度，因此进行一个取余的操作
        # 比如 k = 1000，len = 999
        # 实际上就是将链表每个节点向右移动 1000 % 999 = 1 个位置就行了
        # 因为链表中的每个节点移动 len 次会回到原位
        k = k % _len
        

        # 4、接下来设置两个指针指向链表的头节点
        # 这两个指针的目的是去寻找出旋转之前的尾节点位置、旋转成功之后的尾节点位置

        # former 指针
        former = head

        # latter 指针
        latter = head

        # former 指针先向前移动 k 次
        for i in range(0 , k ) :

            # former 不断向后移动
            former = former.next


        # 这样 former 和 latter 就相差了 k 个节点
        # 5、接下来，两个指针同时向后移动，直到 former 来到了最后一个节点位置
        while former.next :

            # former 不断向后移动
            former = former.next

            # latter 不断向后移动
            latter = latter.next 


        # 6、此时，former 指向了最后一个节点，需要将这个节点和原链表的头节点连接起来
        former.next = head

        # 7、latter 指向的节点的【下一个节点】是倒数第 k 个节点，那就是旋转成功之后的头节点
        newHead = latter.next

        # 8、断开链接，避免成环
        latter.next = None

        # 9、返回 newHead
        return newHead
'''
# @lc code=end

