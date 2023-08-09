#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(-1)
        pre=dummy

        while list1 and list2:
            if list1.val<list2.val:
                pre.next=list1
                list1=list1.next
            else:
                pre.next=list2
                list2=list2.next
            pre=pre.next 
        if list1 is None:
            pre.next=list2
        if list2 is None:
            pre.next=list1
        return dummy.next


'''
// 登录 AlgoMooc 官网获取更多算法图解
// https://www.algomooc.com
// 作者：程序员吴师兄
// 代码有看不懂的地方一定要私聊咨询吴师兄呀
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        # 一开始设置一个虚拟节点，它的值为 -1，它的值可以设置为任何的数，因为我们根本不需要使用它的值
        dummy = ListNode(-1)

        # 设置一个指针，指向虚拟节点
        pre = dummy

        # 通过一个循环，不断的比较 l1 和 l2 中当前节点值的大小，直到 l1 或者 l2 遍历完毕为止
        while l1 and l2: # 不要用!=None因为默认了 !=None
            # 如果 l1 当前节点的值小于等于了 l2 当前节点的值
            if l1.val <= l2.val :
                # 让 pre 指向节点的 next 指针指向这个更小值的节点
                # 即指向 l1
                pre.next = l1
                # 让 l1 向后移动
                l1 = l1.next
            else:
                # 让 pre 指向节点的 next 指针指向这个更小值的节点
                # 即指向 l2
                pre.next =l2
                # 让 l2 向后移动
                l2 = l2.next
            
            # 让 pre 向后移动 易忘！
            pre = pre.next 
        

        # 跳出循环后，l1 或者 l2 中可能有剩余的节点没有被观察过
        # 直接把剩下的节点加入到 pre 的 next 指针位置
        
        # 如果 l1 中还有节点
        if l1 != None :
            # 把 l1 中剩下的节点全部加入到 pre 的 next 指针位置
            pre.next = l1
        

        # 如果 l2 中还有节点
        if l2 != None :
            # 把 l2 中剩下的节点全部加入到 pre 的 next 指针位置
            pre.next = l2;
        

        # 最后返回虚拟节点的 next 指针
        return dummy.next
'''
# @lc code=end

