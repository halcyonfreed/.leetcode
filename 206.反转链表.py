
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      # cur=head
      # pre=None
      # while cur:
      #      tmp=cur.next
      #      cur.next=pre
      #      # 移动
      #      pre=cur
      #      cur=tmp
      # return pre #因为cur走到了NULL，cur==NULL才停下来，所以此时pre是新头
      return self.reverse(head,None)
    def reverse(self,cur:Optional[ListNode],pre: Optional[ListNode]) ->Optional[ListNode]:
      if cur==None:
          return pre # 最终返回的 是pre！！！
      temp=cur.next
      cur.next=pre
      
      return self.reverse(temp,cur) # 往后移动，一直套娃！！！
         



'''
（版本一）双指针法
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head   
        pre = None
        while cur:
            temp = cur.next # 保存一下 cur的下一个节点，因为接下来要改变cur->next
            cur.next = pre #反转
            #更新pre、cur指针
            pre = cur
            cur = temp
        return pre
'''


'''
#  登录 AlgoMooc 官网获取更多算法图解
#  https://www.algomooc.com
#  作者：程序员吴师兄
#  代码有看不懂的地方一定要私聊咨询吴师兄呀
class Solution(object):
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

