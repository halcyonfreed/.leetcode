/*
 * @lc app=leetcode.cn id=641 lang=cpp
 *
 * [641] 设计循环双端队列
 */

// @lc code=start
class MyCircularDeque {
public:
    int capacity,front,rear;
    vector<int> arr;

    MyCircularDeque(int k) {
        capacity=k+1;
        arr=vector<int>(capacity);
        front=0;
        rear=0;
    }
    
    bool insertFront(int value) {
        if (isFull()){
            return false;
        }
        front=(front-1+capacity)%capacity;
        arr[front]=value;
        return true;
    }
    
    bool insertLast(int value) {
        if(isFull()){
            return false;
        }
        arr[rear]=value;
        rear=(rear+1)%capacity;
        return true;
    }
    
    bool deleteFront() {
        if(isEmpty()){
            return false;
        }
        front=(front+1)%capacity;
        return true;
    }
    
    bool deleteLast() {
        if (isEmpty()){
            return false;
        }
        rear=(rear-1+capacity)%capacity;
        return true;
    }
    
    int getFront() {
        if(isEmpty()){
            // 队列为空的话那就没有元素可选，根据题目要求返回 -1
            return - 1;
        }        
        return arr[front];
    }
    
    int getRear() {
        if(isEmpty()) return -1;
        return arr[(rear-1+capacity)%capacity];
    }
    
    bool isEmpty() {
        return front==rear;
    }
    
    bool isFull() {
        return (rear+1)%capacity==front;
    }
};

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque* obj = new MyCircularDeque(k);
 * bool param_1 = obj->insertFront(value);
 * bool param_2 = obj->insertLast(value);
 * bool param_3 = obj->deleteFront();
 * bool param_4 = obj->deleteLast();
 * int param_5 = obj->getFront();
 * int param_6 = obj->getRear();
 * bool param_7 = obj->isEmpty();
 * bool param_8 = obj->isFull();
 * 
 * 
 * // 登录 AlgoMooc 官网获取更多算法图解
// https://www.algomooc.com
// 作者：程序员吴师兄
class MyCircularDeque {

public:
    // capacity 表示数组的容量，它的大小为 k + 1
    int capacity;

    // front 表示队头的位置
    int front;

    // rear 表示队列尾部的下一个位置
    int rear;

    // 这里使用数组来设计循环双端队列
    vector<int> arr;


    MyCircularDeque(int k) {

        // 需要空出一个额外的空间
        // 当队列中的元素有 k 个时，代表队列已满
        capacity = k + 1;

        // 这里使用数组来设计循环双端队列，数组的容量为 capacity
        // 即在数组中会空出一个额外的空间来不存储任何元素
        // 因为这样才能合理的区分出【队列为空】和【队列已满】这两种情况
        arr = vector<int>(capacity);

        // 初始化队头指针
        front = 0;

        // 初始化队尾指针
        rear = 0;
    }

    // 在双端队列的队头添加元素 value
    bool insertFront(int value) {
        // 首先判断队列是否已满，没有其它的剩余空间
        // 如果队列已满，那么元素无法添加进去
        if(isFull()){
           //  返回 false
           return false;
        }

        // front 向前移动
        // 由于 front 会移动到数组的最前面，如果再向前移动会出界
        // 那么这个时候就需要将 front 挪到数组结尾的位置
        // 可以通过取余运算来实现循环移动的这个操作
        // front+capacity-1就是rear的位置！！
        front =  ( front - 1 + capacity ) % capacity;

        // 添加元素 value 到 front 这个位置
        arr[front] = value;

        // 添加元素成功，返回 true
        return true;

    }

    // 在双端队列的队尾添加元素 value
    bool insertLast(int value) {

        // 首先判断队列是否已满，没有其它的剩余空间
        // 如果队列已满，那么元素无法添加进去
        if(isFull()){
           //  返回 false
           return false;
        }

        // 添加元素 value 到 rear 这个位置
        arr[rear] = value;

        // rear 向后移动
        // 由于 rear 会移动到数组的最尾部，如果再向后移动会出界
        // 那么这个时候就需要将 rear 挪到数组开头的位置
        // 可以通过取余运算来实现循环移动的这个操作
        rear =  (rear + 1) % capacity;

        // 添加元素成功，返回 true
        return true;

    }

    // 删除双端队列的队头元素
    bool deleteFront() {
        // 首先判断队列是否为空
        if(isEmpty()){
            // 队列为空的话那就没有元素可删，返回 false
           return false;
        }

        // 队头指针向后移动
        front = (front + 1) % capacity;

        // 删除元素成功，返回 true
        return true;

    }

    // 删除双端队列的队尾元素
    bool deleteLast() {
        // 首先判断队列是否为空
        if(isEmpty()){
            // 队列为空的话那就没有元素可删，返回 false
            return false;
        }

        // 队尾指针向前移动
        rear = (rear - 1 + capacity) % capacity;

        // 删除元素成功，返回 true
        return true;
    }

    int getFront() {
        // 首先判断队列是否为空
        if(isEmpty()){
            // 队列为空的话那就没有元素可选，根据题目要求返回 -1
            return - 1;
        }

        // 否则返回 front 指向的元素就行
        return arr[front];

    }

    int getRear() {
        // 首先判断队列是否为空
        if(isEmpty()){
            // 队列为空的话那就没有元素可选，根据题目要求返回 -1
            return -1;
        }

        // 否则返回 rear 位置的前一个元素就行
        return arr[(rear - 1 + capacity) % capacity];
    }

    // 判断队列是否为空
    bool isEmpty() {
        // front 和 rear 指向同一个位置时，队列为空
        return front == rear;
    }

    bool isFull() {
        // 当队尾指针向后移动一个位置后，指向了队头时，那么说明队列已满
        return (rear + 1) % capacity == front;
    }
};
 */
// @lc code=end

