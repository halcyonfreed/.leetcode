/*
 * @lc app=leetcode.cn id=2 lang=cpp
 *
 * [2] 两数相加
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    

    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *dummmy=new ListNode(-1); 
        int carryBit=0;//进位

        ListNode *cur=dummy;
        while(l1!=nullptr || l2!=nullptr){
            int x;
            if(l1==nullptr){
                x=0;
            }
            else{
                x=l1->val;
            }

            int y;
            if(l2==nullptr){
                y=0;
            }
            else y=l2->val;
        }

        int sum=x+y+carryBit;
        carryBit=sum/10; //存十位类似，进位就是

        int digit=sum%10; //存个位
        ListNode *digitNode=new ListNode(digit);
        cur->next=digitNode;
        cur=cur->next;

        if(l1!=nullptr) l1=l1->next;
        if(l2!=nullptr) l2=l2->next;

    if (carryBit==1){
        ListNode *carryBitNode=new ListNode(carryBit);
        cur->next=carryBitNode;
    }
    return dummy->next;
    }
};
/*
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {

        // 构建一个链表用来存放 l1 和 l2 两个链表相加的结果
        // 其中 dummy 这个节点为虚拟头结点
        ListNode *dummy = new ListNode(-1);

        // 设置一个进位，初始化为 0
        // 两个个位数相加，进位只能是 1 或者 0
        // 比如 7 + 8 = 15，进位是 1
        // 比如 2 + 3 = 6，没有进位，或者说进位是 0
        int carryBit = 0;

        // l1 和 l2 有可能为空，所以先默认结果链表从虚拟头结点位置开始
        ListNode *cur = dummy;

        // 同时遍历 l1 和 l2
        // 只要此时 l1 和 l2 两个链表中的任意链表中节点有值，就一直加下去
        // 直到两个链表中的所有节点都遍历完毕为止
        while(l1 != NULL || l2 != NULL) {
            // 获取 l1 链表中节点的值
            int x;

            // 观察此时 l1 中的节点是否有值
            // 如果节点不存在，那么就用 0 来占位
            if( l1 == NULL){
                // 用 0 来占位
                x = 0;
            }else{
                // 否则，将 l1 的节点值赋值给 x
                x = l1->val;
            }

            // 获取 l2 链表中节点的值
            int y;

            // 观察此时 l2 中的节点是否有值
            // 如果节点不存在，那么就用 0 来占位
            if( l2 == NULL){
                // 用 0 来占位
                y = 0;
            }else{
                // 否则，将 l2 的节点值赋值给 y
                y = l2->val;
            }
   
            // 每一位计算的同时需要考虑上一位的进位情况
            int sum = x + y + carryBit;
            
            // 获取当前计算结果的十位数
            // 比如 7 + 8 = 15
            // 那么 sum / 10 = 1，进位为 1
            carryBit = sum / 10;

            // 获取当前计算结果的个位数
            // 比如 7 + 8 = 15
            // 那么 sum % 10 = 5
            int digit = sum % 10;

            // 构建一个节点用来存放这个个位数
            ListNode *digitNode = new ListNode(digit);

            // 把这个节点加入到结果链表中
            cur->next = digitNode;

            // 移动 cur 的位置，观察后面应该存放什么节点
            cur = cur->next;
            
            // l1 链表中还有节点未遍历完毕就继续遍历下去
            if(l1 != NULL) l1 = l1->next;

            // l2 链表中还有节点未遍历完毕就继续遍历下去
            if(l2 != NULL) l2 = l2->next;
        }

        // 两个链表的尾节点相加之后，有可能产生进位的情况
        // 所以，需要构建一个新的节点用来存放这个进位的结果
        if(carryBit == 1) {
            // 构建一个节点用来存放这个进位
            ListNode *carryBitNode = new ListNode(carryBit);

            // 把这个节点加入到结果链表中
            cur->next = carryBitNode;
        }

        // 最后返回结果链表的头节点就行，即虚拟头结点的下一个节点
        return dummy->next;

    }
};
*/
// @lc code=end

