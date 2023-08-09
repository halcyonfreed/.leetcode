#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#

# @lc code=start
class ALNode:
    def __init__(self, val):
        self.val = val
        self.nextNode = None
        self.preNode = None

class LRUCache:
    def __init__(self, capacity: int):
        self.maps = {}
        self.head = ALNode(-1)
        self.tail = ALNode(-1)
        self.capacity = capacity
        self.length = 0
        self.head.nextNode = self.tail
        self.tail.preNode = self.head

    def get(self, key: int) -> int:
        if key in self.maps:
            cur = self.maps[key][0]
            preNode = cur.preNode
            nextNode = cur.nextNode
            preNode.nextNode = nextNode
            nextNode.preNode = preNode
            tmp = self.head.nextNode
            self.head.nextNode = cur
            cur.nextNode = tmp
            tmp.preNode = cur
            cur.preNode = self.head
            return self.maps[key][1]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.maps:
            cur = self.maps[key][0]
            preNode = cur.preNode
            nextNode = cur.nextNode
            preNode.nextNode = nextNode
            nextNode.preNode = preNode
            tmp = self.head.nextNode
            self.head.nextNode = cur
            cur.nextNode = tmp
            tmp.preNode = cur
            cur.preNode = self.head
            self.maps[key] = [cur, value]
            return
        if self.length == self.capacity:
            delNode = self.tail.preNode
            delPreNode = self.tail.preNode.preNode
            delPreNode.nextNode = self.tail
            self.tail.preNode = delPreNode
            del self.maps[delNode.val]
            self.length -= 1
        cur = ALNode(key)
        tmp = self.head.nextNode
        self.head.nextNode = cur
        cur.nextNode = tmp
        tmp.preNode = cur
        cur.preNode = self.head
        self.maps[key] = [cur, value]
        self.length += 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

