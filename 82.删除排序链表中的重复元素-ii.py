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
        # dummy=ListNode(-1)
        # dummy.next=head
        # cur=dummy

        # while cur.next and cur.next.next:
        #     if cur.next.val==cur.next.next.val:
        #         value=cur.next.val
        #         while cur.next and cur.next.val==value:
        #             cur.next=cur.next.next
        #     else:
        #         cur=cur.next
        # return dummy.next

        if head==None or head.next==None:
            return head
        
        if head.val!=head.next.val:
            resNode=self.deleteDuplicates(head.next) # 套娃，返回已经处理完的下一个头
            head.next=resNode
            return head
        else:
            newNode=head.next # 当前会和后面一样，所以删了
            # 然后一直找，直到找到不一样的了
            while newNode!=None and head.val==newNode.val:
                newNode=newNode.next
        return self.deleteDuplicates(newNode)

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

法二
# 登录 AlgoMooc 官网获取更多算法图解
# https://www.algomooc.com
# 作者：程序员吴师兄
# 代码有看不懂的地方一定要私聊咨询吴师兄呀
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/submissions/
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 递归终止条件
        if head == None or head.next == None:
            return head
        

        # 在访问过程中，会出现两种情况
        # 1、如果访问的节点值和下一个节点值不相同
        if head.val != head.next.val:

            # 那么说明当前访问的节点 head 需要保留下来，它和后面经过删除操作的链表连接起来

            # a、利用递归，获取后续删除了链表重复元素的链表
            resNode = self.deleteDuplicates(head.next)

            # 将 head 和后续已经删除了重复元素的链表连接起来
            head.next = resNode

            # 返回这个结果就行
            return head

        # 2、如果访问的节点值和下一个节点值相同
        else:

            # 那说明 head 这个节点就不应该留下来

            # 现在的目的就是去找出和 head 这个节点值不一样的节点来
            newNode = head.next

            # 利用 while 循环，找出和 head 这个节点值不一样的节点来
            while newNode != None and head.val == newNode.val:
                newNode = newNode.next
            

            # 此时，经过 while 循环后，newNode 指向了一个不等于 head 的节点
            # 递归调用 deleteDuplicates 函数，处理后面的所有节点
            # 处理好后
            # 1、要么是直接是最终的结果
            # 2、要么是这个结果链表会连接在某个节点后面，比如上述的 a 操作这行代码
            return self.deleteDuplicates(newNode)
'''
# @lc code=end

