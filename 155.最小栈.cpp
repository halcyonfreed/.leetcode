/*
 * @lc app=leetcode.cn id=155 lang=cpp
 *
 * [155] 最小栈
 */

// @lc code=start
class MinStack {
public:
    stack<int> stk;
    stack<int> minstk;
    MinStack() {
    }//类似init
    
    void push(int val) {
        stk.push(val);
        if (!minstk.empty()){
            int top=minstk.top();
            if (val<=top){
                minstk.push(val);
            }
        }
        else{
            minstk.push(val);
        }
    }
    
    void pop() {
        int pop=stk.top();
        stk.pop();
        if(pop==minstk.top()){
            minstk.pop();
        }
    }
    
    int top() {
        return stk.top();
    }
    
    int getMin() {
        return minstk.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
/*
时间复杂度：对于题目中的所有操作，时间复杂度均为 O(1)。因为栈的插入、删除与读取操作都是 O(1)，我们定义的每个操作最多调用栈操作两次。
空间复杂度：O(n)，其中 n 为总操作数。最坏情况下，我们会连续插入 n 个元素，此时两个栈占用的空间为 O(n)。

// 登录 AlgoMooc 官网获取更多算法图解
// https://www.algomooc.com
// 作者：程序员吴师兄
// 代码有看不懂的地方一定要私聊咨询吴师兄呀
// 最小栈（ LeetCode 155 ）:https://leetcode-cn.com/problems/min-stack/
class MinStack {
public:
    // 首先定义好两个栈

    // 一个栈叫做 stk
    stack<int> stk;

    // 一个栈叫做 minstk，负责获取 stk 中的最小值，它等价于遍历 stk 中的所有元素，把升序的数字都删除掉，留下一个从栈底到栈顶降序的栈
    stack<int> minstk;

    MinStack() {    
  
    }

    void push(int x) {
        // 新添加的元素添加到 stk 中
        stk.push(x);

        // 判断 minstk 是否为空，如果为空，直接同时把新添加的元素添加到 minstk 中

        // 如果 minstk 不为空
        if (!minstk.empty()) {
            // 获取 minstk 的栈顶元素
            int top = minstk.top();
            // 只有新添加的元素不大于 top 才允许添加到 minstk 中，目的是为了让 minstk 从栈底到栈顶是降序的
            if (x <= top) {
                // 此时，新添加的元素 x 小于 top，加入到 minstk 后依旧是从栈底到栈顶是降序的
                minstk.push(x);
            }
        }else{
            // 此时，minstk 中没有元素，所以直接把新添加的元素添加到 minstk 中
            minstk.push(x);
        }
    }

    void pop() {
        
        // 让 stk 执行正常的 pop 操作就行
        int pop = stk.top();

        stk.pop();

        // 由于 minstk 中的所有元素都是来自于 stk 中，所以 stk 删除元素后，minstk 也要考虑是否需要删除元素
        // 否则的话，minstk 有可能保存一个 stk 中不存在的元素

        // 首先，获取 minstk 的栈顶元素
        int top = minstk.top();
        // 再判断 top 这个栈顶元素是否和 stk 移除的元素相等，如果相等，那么需要把 minstk 中的栈顶元素一并移除 
        if (pop == top) {
            // 移除 minstk 的栈顶元素
            minstk.pop();
        }

    }

    int top() {
        // 返回 stk 的栈顶元素
        return stk.top();
    }

    int getMin() {
        // 返回 minstk 的栈顶元素
        return minstk.top();
    }
};
*/
// @lc code=end

