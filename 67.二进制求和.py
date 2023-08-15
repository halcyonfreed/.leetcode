#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res=''
        carry=0
        i=len(a)-1
        j=len(b)-1
        while i>=0 or j>=0 or carry!=0:
            digitA=int(a[i]) if i>=0 else 0
            digitB=int(b[j]) if j>=0 else 0

            sum=digitA+digitB+carry
            carry=1 if sum>=2 else 0
            sum=sum-2 if sum>=2 else sum
            i-=1
            j-=1
        return res[::-1] # 反转

'''
// 登录 AlgoMooc 官网获取更多算法图解
// https://www.algomooc.com
// 作者：程序员吴师兄
// 微信：wzb_3377
// 代码有看不懂的地方一定要私聊咨询吴师兄呀
// 二进制求和（LeetCode 67）：https://leetcode.cn/problems/add-binary/
class Solution {
    public String addBinary(String a, String b) {

        // 使用字符串去拼接每一次计算的结果
        StringBuilder ans = new StringBuilder();

        // 二进制计算过程中产生的进位
        int carry = 0;

        // 开始计算
        for(int i = a.length() - 1, j = b.length() - 1;i >= 0 || j >= 0; i--, j--) {
            
            // 获取字符串 a 中对应的字符，如果有，那就是 a.charAt(i) - '0' 这个数字，否则设置为 0
            int numA = i >= 0 ? a.charAt(i) - '0' : 0;

            // 获取字符串 b 中对应的字符，如果有，那就是 b.charAt(i) - '0' 这个数字，否则设置为 0
            int numB = j >= 0 ? b.charAt(j) - '0' : 0;

            // 每次计算的过程都是 字符串 a 对应的字符 + 字符串 b 对应的字符 + 前面产生的进位
            // 这里采取的是【十进制】的计算规则，比如 1 + 1 = 2
            int sum = numA + numB + carry;
            
            // 需要把 sum 拆解为二进制的形式，比如十进制的结果 2 为二进制的 10
            // 通过 %2 的操作，可以把 0 存储到 ans 中
            ans.append(sum % 2);

            // 通过 /2 的操作，可以把 1 存储到 carry 中
            carry = sum / 2;

        }

        // 最后，需要观察最后的计算过程中是否还有进位没有使用到
        ans.append(carry == 1 ? carry : "");

        // 由于整个计算过程是从后向前计算，导致低位的计算结果存储在 ans 的前面
        // 所以需要翻转一下
        return ans.reverse().toString();
    }
}


class Solution(object):
    def addBinary(self, a, b):
        res = ""
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 or j >= 0 or carry != 0:
            digitA = int(a[i]) if i >= 0 else 0
            digitB = int(b[j]) if j >= 0 else 0
            sum = digitA + digitB + carry
            carry = 1 if sum >= 2 else 0
            sum = sum - 2 if sum >= 2 else sum
            res += str(sum)
            i -= 1
            j -= 1
        return res[::-1]
'''
# @lc code=end

