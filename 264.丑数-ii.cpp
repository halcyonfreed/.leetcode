/*
 * @lc app=leetcode.cn id=264 lang=cpp
 *
 * [264] 丑数 II
 */

// @lc code=start
class Solution {
public:
    int nthUglyNumber(int n) {
        vector<int> factors = {2, 3, 5};
        unordered_set<long> seen;
        priority_queue<long, vector<long>, greater<long>> pq; //升序优先队列，小顶堆

        seen.insert(1L);
        pq.push(1L);
        int ugly = 1;
        for (int i = 0; i < n; i++) {
            long curr = pq.top();
            pq.pop();
            ugly = (int) curr;
            for (int factor : factors) {
                long next = curr * factor;
                if (!seen.count(next)) {
                    seen.insert(next);
                    pq.push(next);
                }
            }
        }
        return ugly;
    }
};
/*
class Solution {
public:
    int nthUglyNumber(int n) {

        // 对任意一个丑数来说，去和 2、3、5 分别相乘，可以得到 3 个丑数
        // 那么对每一个丑数都去和 2 、3 、5 分别相乘，把那些结果进行排序即可
        // 因此，2、3、5 就是我们需要处理的质因数
        vector<int> factors = {2, 3, 5};

        // 由于一些丑数和 2 、 3 、5 相乘会出现重复元素的情况
        // 比如丑数 2 和 2 、 3 、5 相乘得到了 4、【6】、10
        // 而丑数 3 和 2 、 3 、5 相乘得到了 【6】、9 、 15
        // 其中 【6】重复了，所以需要采取去重操作
        // 由于题目说明 n 最大为 1690，会导致丑数的范围超过了 int 范围，所以使用 long 来保存
        unordered_set<long> seen;

        // 使用优先队列来获取每次集合中最小的数字
        // 由于题目说明 n 最大为 1690，会导致丑数的范围超过了 int 范围，所以使用 long 来保存
        priority_queue<long, vector<long>, greater<long>> pq;
        
        // 集合中第一个数字是 1
        // 常量后面跟这种一般是指类型
        // 1L 表示 1 是长整型，如果是 1f 表示是 float 型
        seen.insert(1L);

        // 优先队列里面的元素来源于 seen
        pq.push(1L);

        // 开始不断的迭代丑数的值，直到迭代了 n 次为止
        // 第一个丑数是 1
        int ugly = 1;

        // 开始迭代
        for (int i = 0; i < n; i++) {

            // 下一个丑数来源于优先队列的队头元素
            long curr = pq.top();

            pq.pop();

            // 本题需要返回 int 型，所以强转一下
            ugly = (int) curr;

            // 再将获取到的丑数和 2 、3 、5 分别相乘
            for (int factor : factors) {

                // 获取到新的丑数
                long next = curr * factor;

                // 经过去重操作后
                if (!seen.count(next)) {
                    // 把这个丑数加入到优先队列里面
                    // 优先队列里面会自动操作，使得最小的元素位于队头
                    seen.insert(next);
                    pq.push(next);
                }
            }
        }

        // 返回结果
        return ugly;

    }
};
*/
// @lc code=end

