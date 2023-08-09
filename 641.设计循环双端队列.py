#
# @lc app=leetcode.cn id=641 lang=python3
#
# [641] 设计循环双端队列
#

# @lc code=start
class MyCircularDeque:
    '''
    反正就是所有的rear-1要取模；front-1也要取模
    '''
    def __init__(self, k: int):
        self.capacity=k+1
        self.arr=[0]*self.capacity
        self.front=0
        self.rear=0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        # 本质上就是front-1，只不过因为循环队列，所以-1可能会到头指不到任何东西，所以可以加capacity，再取模
        # front先动再插，因为front本身有value
        self.front=((self.front-1)+self.capacity)%self.capacity
        self.arr[self.front]=value
        return True
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        # rear本身没value,所以先插值，再动
        self.arr[self.rear]=value
        self.rear=(self.rear+1)%self.capacity
        return True
    
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front=(self.front+1)%self.capacity
        return True   
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        # rear-1可能会到头，所以要加self.capacity
        self.rear=((self.rear-1)+self.capacity)%self.capacity 
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.front]
    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[((self.rear-1)+self.capacity)%self.capacity]
    
    def isEmpty(self) -> bool:
        return self.front==self.rear
    def isFull(self) -> bool:
        # return ((self.rear+1)+self.capacity)%self.capacity==self.front
        return (self.rear+1)%self.capacity==self.front



# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
'''
# 登录 AlgoMooc 官网获取更多算法图解
# https://www.algomooc.com
# 作者：程序员吴师兄
class MyCircularDeque:

    # capacity 表示数组的容量，它的大小为 k + 1

    # front 表示队头的位置

    # rear 表示队列尾部的下一个位置

    # 这里使用数组来设计循环双端队列

    def __init__(self, k: int):

        # 需要空出一个额外的空间
        # 当队列中的元素有 k 个时，代表队列已满
        self.capacity = k + 1

        # 这里使用数组来设计循环双端队列，数组的容量为 capacity
        # 即在数组中会空出一个额外的空间来不存储任何元素
        # 因为这样才能合理的区分出【队列为空】和【队列已满】这两种情况
        self.arr = [0] * self.capacity

        # 初始化队头指针
        self.front = 0

        # 初始化队尾指针
        self.rear = 0
    

    # 在双端队列的队头添加元素 value
    def insertFront(self, value: int) -> bool:
        # 首先判断队列是否已满，没有其它的剩余空间
        # 如果队列已满，那么元素无法添加进去
        if self.isFull() :
           #  返回 false
           return False

        # front 向前移动
        # 由于 front 会移动到数组的最前面，如果再向前移动会出界
        # 那么这个时候就需要将 front 挪到数组结尾的位置
        # 可以通过取余运算来实现循环移动的这个操作
        self.front =  ( self.front - 1 + self.capacity ) % self.capacity

        # 添加元素 value 到 front 这个位置
        self.arr[self.front] = value

        # 添加元素成功，返回 true
        return True

    # 在双端队列的队尾添加元素 value
    def insertLast(self, value: int) -> bool:

        # 首先判断队列是否已满，没有其它的剩余空间
        # 如果队列已满，那么元素无法添加进去
        if self.isFull() :
           #  返回 false
           return False

        # 添加元素 value 到 rear 这个位置
        self.arr[self.rear] = value

        # rear 向后移动
        # 由于 rear 会移动到数组的最尾部，如果再向后移动会出界
        # 那么这个时候就需要将 rear 挪到数组开头的位置
        # 可以通过取余运算来实现循环移动的这个操作
        self.rear =  (self.rear + 1) % self.capacity

        # 添加元素成功，返回 true
        return True


    # 删除双端队列的队头元素
    def deleteFront(self) -> bool:
        # 首先判断队列是否为空
        if self.isEmpty():
            # 队列为空的话那就没有元素可删，返回 false
            return False

        # 队头指针向后移动
        self.front = (self.front + 1) % self.capacity

        # 删除元素成功，返回 true
        return True
 

    # 删除双端队列的队尾元素
    def deleteLast(self) -> bool:
        # 首先判断队列是否为空
        if self.isEmpty():
            # 队列为空的话那就没有元素可删，返回 false
            return False

        # 队尾指针向前移动
        self.rear = (self.rear - 1 + self.capacity) % self.capacity

        # 删除元素成功，返回 true
        return True
    

    def getFront(self) -> int:
        if self.isEmpty():
            # 队列为空的话那就没有元素可选，根据题目要求返回 -1
            return -1

        # 否则返回 front 指向的元素就行
        return self.arr[self.front]

    def getRear(self) -> int:
        # 首先判断队列是否为空
        if self.isEmpty():
            # 队列为空的话那就没有元素可选，根据题目要求返回 -1
            return -1

        # 否则返回 rear 位置的前一个元素就行
        return self.arr[(self.rear - 1 + self.capacity) % self.capacity]
    

    # 判断队列是否为空
    def isEmpty(self) -> bool:
        # front 和 rear 指向同一个位置时，队列为空
        return self.front == self.rear
    

    def isFull(self) -> bool:
        # 当队尾指针向后移动一个位置后，指向了队头时，那么说明队列已满
        return (self.rear + 1) % self.capacity == self.front
'''
# @lc code=end

