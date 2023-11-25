#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#
class ListNode:
    def __init__(self,val=0,next=None):
        # 默认指向空指针
        self.val=val
        self.next=next

class MyLinkedList:

    # 有Index都要判断合法性
    def __init__(self):
        self.dummy_head=ListNode() # 创建新的linked-list，以dummyhead开头
        self.size=0
    
    def get(self,index:int)->int:
        # 先处理特殊情况
        if index<0 or index>=self.size:
            # index=size就无效了已经
            return -1
        cur=self.dummy_head.next # 从dummyhead.next开始遍历，dummyhead本来就不是list里的
        for i in range(index):
            cur=cur.next
        return cur.val
    

# cur都从dummyhead开始，操作的是cur.next
    def addAtHead(self,val:int)->None:
        # 就从头开始，所以不用找位置先
        # c++下面两行分开，python可以合起来！！！ self.dummy_head.next=ListNode(val,self.dummy_head.next)
        newnode=ListNode(val,self.dummy_head.next) # 先赋值
        self.dummy_head.next=newnode # 再指
        self.size+=1

    def addAtTail(self,val:int)->None:
        cur=self.dummy_head # 有可能本来就是空，操作cur.next不是cur，所以从dummyhead不是dummyhead.next开始
        # while cur.next:
        #     # 忘记用的是while，for可以嘛
        #     cur=cur.next
        
        for _ in range(self.size):
            cur=cur.next

        newnode=ListNode(val) # 默认next=None空指针
        cur.next=newnode
        self.size+=1
    def addAtIndex(self,index:int,val:int)->None:
        if index<0 or index>self.size:
            return
        cur=self.dummy_head
        for _ in range(index):
            cur=cur.next
        newnode=ListNode(val,cur.next)
        cur.next=newnode

        self.size+=1
    
    def deleteAtIndex(self,index:int)->None:
        if index<0 or index>=self.size:
            # index=size已经不行 =size-1才行！！
            return -1
         
        cur=self.dummy_head # 删掉需要借助上一个，所以=dummyhead不是next
        for _ in range(index):
            cur=cur.next
        cur.next=cur.next.next
        self.size-=1

    

# （版本一）单链表法
'''class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class MyLinkedList:
    def __init__(self):
        self.dummy_head = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        current = self.dummy_head.next
        for i in range(index):
            current = current.next
            
        return current.val

    def addAtHead(self, val: int) -> None:
        self.dummy_head.next = ListNode(val, self.dummy_head.next)
        self.size += 1

    def addAtTail(self, val: int) -> None:
        current = self.dummy_head
        while current.next:
            current = current.next
        current.next = ListNode(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        
        current = self.dummy_head
        for i in range(index):
            current = current.next
        current.next = ListNode(val, current.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        current = self.dummy_head
        for i in range(index):
            current = current.next
        current.next = current.next.next
        self.size -= 1


'''# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end