/*
 * @lc app=leetcode.cn id=232 lang=cpp
 *
 * [232] 用栈实现队列
 */

// @lc code=start
class MyQueue {
public:
    stack<int> stackIn,stackOut;
    MyQueue() {
    }
    
    void push(int x) {
        stackIn.push(x);
    }
    
    int pop() {
        if (stackOut.empty()){
            while(!stackIn.empty()){
                int pop=stackIn.top();
                stackIn.pop();
                stackOut.push(pop);
            }
        }
        int pop=stackOut.top();
        stackOut.pop();
        return pop;
    }
    
    int peek() {
        if (stackOut.empty()){
            while(!stackIn.empty()){
                int pop=stackIn.top();
                stackIn.pop();
                stackOut.push(pop);
            }
        }
        return stackOut.top();
    }
    
    bool empty() {
        return stackIn.empty() && stackOut.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
// @lc code=end

