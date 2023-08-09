/*
 * @lc app=leetcode.cn id=146 lang=cpp
 *
 * [146] LRU 缓存
 */

// @lc code=start
class LRUCache {
public:
    LRUCache(int capacity) {

    }
    
    int get(int key) {

    }
    
    void put(int key, int value) {

    }
};

/*
class ALNode {
public:
    int val;
    ALNode* nextNode;
    ALNode* preNode;
    
    ALNode(int val) {
        this->val = val;
        nextNode = nullptr;
        preNode = nullptr;
    }
};

class LRUCache {
public:
    unordered_map<int, pair<ALNode*, int>> maps;
    ALNode* head;
    ALNode* tail;
    int capacity;
    int length;

    LRUCache(int capacity) {
        head = new ALNode(-1);
        tail = new ALNode(-1);
        this->capacity = capacity;
        length = 0;
        head->nextNode = tail;
        tail->preNode = head;
    }

    int get(int key) {
        if (maps.count(key)) {
            ALNode* cur = maps[key].first;
            ALNode* preNode = cur->preNode;
            ALNode* nextNode = cur->nextNode;
            preNode->nextNode = nextNode;
            nextNode->preNode = preNode;
            ALNode* tmp = head->nextNode;
            head->nextNode = cur;
            cur->nextNode = tmp;
            tmp->preNode = cur;
            cur->preNode = head;
            return maps[key].second;
        }
        return -1;
    }

    void put(int key, int value) {
        if (maps.count(key)) {
            ALNode* cur = maps[key].first;
            ALNode* preNode = cur->preNode;
            ALNode* nextNode = cur->nextNode;
            preNode->nextNode = nextNode;
            nextNode->preNode = preNode;
            ALNode* tmp = head->nextNode;
            head->nextNode = cur;
            cur->nextNode = tmp;
            tmp->preNode = cur;
            cur->preNode = head;
            maps[key].second = value;
            return;
        }
        if (length == capacity) {
            ALNode* delNode = tail->preNode;
            ALNode* delPreNode = delNode->preNode;
            delPreNode->nextNode = tail;
            tail->preNode = delPreNode;
            maps.erase(delNode->val);
            length--;
            delete delNode;
        }
        ALNode* cur = new ALNode(key);
        ALNode* tmp = head->nextNode;
        head->nextNode = cur;
        cur->nextNode = tmp;
        tmp->preNode = cur;
        cur->preNode = head;
        maps[key] = make_pair(cur, value);
        length++;
    }
};
*/
/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
// @lc code=end

