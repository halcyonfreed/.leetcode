#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        map=collections.defaultdict(int)

        for ch in t :
            map[ch]+=1
        whindowLength=len(s)+1
        left,right=0,0
       
        count=len(t)
        start=0


        while right<len(s):
            c=s[right]
            if map[c]>0:
                count-=1
            map[c]-=1

            while count==0:
                if right-left+1<whindowLength:
                    whindowLength=right-left+1
                    start=left

                if map[s[left]]==0:
                    count+=1
                map[s[left]]+=1
                left+=1
            right+=1
        return '' if whindowLength==(len(s)+1) else s[start:start+whindowLength]
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 使用整型数组来表示每个字符在 t 中的数量，初始化都为 0，利用 ASCII 码的方式把字符存储到整型数组中
        # 数组的长度设置为 128
        # 其中 65 ～ 90 号为 26 个大写英文字母，97 ～ 122 号为 26 个小写英文字母，其余为一些标点符号、运算符号等
        # 由于 t 是由英文字母组成，所以数组中有些位置的值始终不会被操作，造成了空间的浪费，比如 map[20]map[30]
        # 但这样做方便理解，比如看到 map[98] = 5 ，能知道 b 出现的频次是 5 次
        map = collections.defaultdict(int)


        # 开始统计 t 中每个字符出现的频次
        for ch in t:   #初始化需要的必要字符数量
            map[ch] += 1

        # 记录滑动窗口的长度，并且不断更新获取最小的那个
        windowLength = len(s) + 1

        # 滑动窗口的左端
        left = 0

        # 滑动窗口的右端
        right = 0

        # t 中字符的总个数
        count = len(t)

        # 滑动窗口左端新的位置
        start = 0

        # 滑动窗口的右端开始移动
        while right < len(s) :

            # 获取此时将要加入到滑动窗口的元素
            c = s[right]

            # 如果说 map 数组中 c 出现的频次大于了 0，说明此时字符 c 加入到滑动窗口距离找到这样一个子串更近了一步
            # 那么滑动窗口需要搜罗的特定元素个数变少了
            if map[c] > 0 : 
                # 需要搜罗的和 t 中字符一样的元素个数变少了
                count -= 1

            # 既然滑动窗口中新增了一个字符 c，那么 map 数组中对应的频次就需要减 1
            map[c] -= 1

        


            # 如果此时 count == 0 ，表明滑动窗口中包含了 t 中全部的字符
            # 此时，找到了一个符合条件的子串
            # 但想尝试一下，能否满足条件的情况下子串更短一些
            # 于是，去尝试把滑动窗口的左端向右移动一下
            # 可以移动的前提是，滑动窗口的左端元素抛弃后剩下的元素依旧满足条件
            # 意思就是实际上左端元素是多余的
            # 而如果这个元素对应的值在 map[] 数组中小于 0，说明它是一个多余元素
            # 反复的删除这些多余的元素
            while count == 0 : 

                # 如果当前的这个窗口值比之前维护的窗口值更小，需要进行更新
                if  right - left + 1 < windowLength : 

                    # 更新滑动窗口的长度
                    windowLength = right - left + 1

                    # 更新滑动窗口起始位置，来到了 left 这个位置
                    start = left
        

                # 接下来左端位置开始向右移动，也就是一个删除操作
                # 删除操作需要执行以下三个步骤
                # 如果这个元素不是多余的元素，比如滑动窗口为 ADBC，t 为 ABC
                # 移除了 A，那么滑动窗口又需要去新增其它的元素了
                # 所以通过 map[s.charAt(left)] == 0 来判断它是否是多余的元素
                if  map[s[left]] == 0 : 
                    # 需要搜罗的和 t 中字符一样的元素个数要增加一个了，因为删除了关键元素
                    count += 1
            
                
                # 2、这个元素离开了滑动窗口，那么在 map 中这个的值就需要加 1
                # 对应着上面新增一个元素到滑动窗口，map[c]--
                map[s[left]] += 1

                # 3、left 向右移动，那么这个元素就离开了
                left += 1

        

            # 可以开始查看新的元素了
            right += 1



        # 根据 s 中是否涵盖了 t 所有字符的子串来获取结果
        return  '' if  windowLength == (len(s) + 1) else s[start:start + windowLength]
'''
# @lc code=end

