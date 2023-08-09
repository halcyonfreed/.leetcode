#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        mid=self.middleNode(head)
        leftHead=head
        rightHead=mid.next

        mid.next=None # 先赋值，在断开
        rightHead=self.reverseList(rightHead)

        # 拼起来
        while leftHead and rightHead:
            # 必须记录next因为移动以后 会有问题！！
            leftHeadNext=leftHead.next
            rightHeadNext=rightHead.next

            leftHead.next=rightHead
            leftHead=leftHeadNext

            rightHead.next=leftHead
            rightHead=rightHeadNext




    def middleNode(self,head:ListNode)->ListNode:
        # 快慢指针找中点
        slow=fast=head # 还能连等这么6
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow # slow正好是左半边的尾节点
    
    def reverseList(self,head):
        if head==None or head.next==None:
            return head
        cur=self.reverseList(head.next) # 妙啊，递归
        head.next.next=head # why????
        head.next=None
        return cur

'''

class Solution:
    def reorderList(self, head: ListNode) -> None:
        # a、寻找出原链表的中点，把链表划分为两个区域
        # b、将右边的链表进行反转
        # c、把这两个区域进行交错合并
      
        # 1、使用快慢指针寻找出链表的中点来 
        # ********
        # 对于 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
        # 中间节点值为 5
        # 所以左边区域为 1 -> 2 -> 3 -> 4 -> 5
        # 右边区域为 6 -> 7 -> 8
        # 但在视频讲解中，我把 5 归为了右边区域，这是一个错误
        # 虽然这个错误并不影响结果，因为合并过程都是一样的逻辑
        # ********
        mid = self.middleNode(head)

        # 2、基于 mid 这个中点，将链表划分为两个区域

        # 左边的区域开头节点是 head
        leftHead = head

        # 右边的区域开头节点是 mid.next
        rightHead = mid.next

        # 将链表断开，就形成了两个链表了
        mid.next = None

        # 3、将右边的链表进行反转
        rightHead = self.reverseList(rightHead)

        # 4、将这两个链表进行合并操作，即进行【交错拼接】
        while leftHead and rightHead :

            # 拼接过程如下
            # 5、先记录左区域、右区域【接下来将有访问的两个节点】
            leftHeadNext = leftHead.next

            rightHeadNext = rightHead.next

            # 6、左边连接右边的开头
            leftHead.next = rightHead

            # 7、leftHead 已经处理好，移动到下一个节点，即刚刚记录好的节点
            leftHead = leftHeadNext

            # 8、右边连接左边的开头
            rightHead.next = leftHead

            # 9、rightHead 已经处理好，移动到下一个节点，即刚刚记录好的节点
            rightHead = rightHeadNext
    


    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 寻找递归终止条件
        # 1、head 指向的结点为 null 
        # 2、head 指向的结点的下一个结点为 null 
        # 在这两种情况下，反转之后的结果还是它自己本身
        if(head == None or head.next == None):
            return head

        # 不断的通过递归调用，直到无法递归下去，递归的最小粒度是在最后一个节点
        # 因为到最后一个节点的时候，由于当前节点 head 的 next 节点是空，所以会直接返回 head
        cur = self.reverseList(head.next)

        # 比如原链表为 1 --> 2 --> 3 --> 4 --> 5
        # 第一次执行下面代码的时候，head 为 4，那么 head.next = 5
        # 那么 head.next.next 就是 5.next ，意思就是去设置 5 的下一个节点
        # 等号右侧为 head，意思就是设置 5 的下一个节点是 4

        # 这里出现了两个 next
        # 第一个 next 是「获取」 head 的下一节点
        # 第二个 next 是「设置」 当前节点的下一节点为等号右侧的值
        head.next.next = head

        # 原来的下一节点指向自己，所以 head 自己本身就不能再指向原来的下一节点了
        # 否则会发生无限循环
        head.next = None

        # 我们把每次反转后的结果传递给上一层
        return cur
'''
# @lc code=end

