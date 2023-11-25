#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # slow=fast=head
        # while fast and fast.next:
        #     slow=slow.next
        #     fast=fast.next.next
        #     if slow==fast:
        #         slow=head # fast别动！！

        #         # 然后slow走x，fast走z=x，它们的第一次相遇就是入口了，return slow
        #         while slow!=fast:
        #             slow=slow.next
        #             fast=fast.next
        #         return slow
            
        # return None
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                slow=head

                while slow!=fast:
                    slow=slow.next
                    fast=fast.next
                return slow
        return None



                


'''
# 登录 AlgoMooc 官网获取更多算法图解
# https://www.algomooc.com
# 作者：程序员吴师兄
# 代码有看不懂的地方一定要私聊咨询吴师兄呀
# 环形链表 II （ LeetCode 142 ） : https://leetcode-cn.com/problems/linked-list-cycle-ii
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 1、通过快慢指针的方式，在环中寻找它们的第一次相遇的节点位置

        # 2、定义一个慢指针，每次只会向前移动 1 步
        slow = head
        # 3、定义一个快指针，每次只会向前移动 2 步
        fast = head

        # 4、如果链表有环，那么无论怎么移动，fast 指向的节点都是有值的
        while fast != None and fast.next != None :
            # 慢指针每次只会向前移动 1 步
            slow = slow.next
            # 快指针每次只会向前移动 2 步
            fast = fast.next.next

            # 快慢指针相遇，说明有环
            # x 代表从头节点到环形入口节点的节点数（不包含头节点）
            # y 代表从环形入口到第一次相遇节点的节点数（不包含环形入口节点）
            # z 代表从第一次相遇节点到环形入口的节点数（不包含第一次相遇节点）
            # y + z 代表环的节点总数
            # 此时，快指针走了 x + y + n y + z)
            # 其中，x + y 表示快指针第一次到达相遇节点，n 代表快指针在环里面绕了多少圈
            # 此时，慢指针走了 x + y 步

            # 由于快指针每次走 2 步，所以快慢指针第一次相遇的时候出现一个等式
            # x + y = [x + y + n y + z)] / 2
            # 即 2 * x + y) = x + y + n y + z)
            # 即 x + y = n（y + z）
            # 即 x = n（y + z）- y
            # 我们的目的就是去求 x
            
            # 定义两个指针，一个指向相遇节点，定义为 b，一个指向链表头节点，定义为 a

            # b 在环中绕圈圈，走了 n（y + z）步会回到原处，即回到相遇节点处
            # 由于 y 代表从环形入口到第一次相遇节点的节点数（不包含环形入口节点）
            # 所以 n（y + z） - y 时，b 到达了环形入口节点位置

            # 由于 x 代表从头节点到环形入口节点的节点数（不包含头节点）
            # 所以 a 走了 x 步时，a 到达了环形入口节点位置

            # 当 x = n（y + z）- y 时，找到了环形入口节点位置

            # 5、开始寻找环入口
            if slow == fast :

                # 定义两个指针，一个指向相遇节点，定义为 b，一个指向链表头节点，定义为 a
                # 一个指向相遇节点，定义为 b
                b = fast

                # 一个指向链表头节点，定义为 a
                a = head

                # 让 a 、b 两个指针向前移动，每次移动一步，直到相遇位置
                # 由于有环，必然相遇
                # 当 b 走了 n（y + z） - y 时，b 到达了环形入口节点位置
                # 当 a 走了 x 步时，a 到达了环形入口节点位置
                # a 与 b 相遇
                while a != b :
                    # a 指针每次只会向前移动 1 步
                    a = a.next
                    # b 指针每次只会向前移动 1 步
                    b = b.next
                

                # 6、返回 a 和 b 相遇的节点位置就是环形入口节点位置
                return a
            
        # 没有环，返回 None
        return None
'''
# @lc code=end

