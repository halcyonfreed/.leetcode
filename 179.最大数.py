#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#

# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs=[str(num) for num in nums]
        self.quickSort(strs,0,len(strs)-1) # left, right是index
        # strs.reverse()
        return ''.join(strs) if strs[0]!='0' else '0' # 没有的补0
    
    def quickSort(self,strs:List[str],left:int,right:int):
        if left>=right:
            return 
        mid=self.partition(strs,left,right)
        self.quickSort(strs,left,mid-1)
        self.quickSort(strs,mid+1,right) # 妙啊，递归套娃
    
    def partition(self,strs:List[str],left:int,right:int)->int:
        pivot=strs[left]
        while left<right:
            # 左边大右边小，降序排
            while left<right and pivot+strs[right]>=strs[right]+pivot:
                right-=1
            strs[left]=strs[right]
            while left<right and strs[left]+pivot>=pivot+strs[left]:
                left+=1
            strs[right]=strs[left]
        strs[left]=pivot
        return left


'''

登录 AlgoMooc 官网获取更多算法图解
# https://www.algomooc.com
# 作者：程序员吴师兄
# 代码有看不懂的地方一定要私聊咨询吴师兄呀
# https://leetcode-cn.com/problems/largest-number/
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        # 先将 nums 转换为字符串数组的形式
        strs = [str(num) for num in nums]

        # 通过快速排序的方式，将字符串数组的每个字符按照约定的顺序进行排序
        self.quickSort(strs,0,len(strs) - 1)

        strs.reverse()
        
        # 再把字符串数组转字符串的形式  
        return ''.join(strs) if strs[0] != '0' else '0'

    # 函数传入待排序数组 nums
    # 排序区间的左端点 left
    # 排序区间的右端点 right
    def quickSort(self,strs: List[str] , left : int ,right : int) : 

        # 如果 left 大于等于 right，说明该区间只有 1 个或者没有元素
        if left >= right :
            # 无需再递归划分后再排序，直接返回
            return
        

        # 调用函数 partition，将 left 和 right 之间的元素划分为左右两部分
        mid = self.partition(strs,left,right)

        # 划分之后，再对 mid 左侧的元素进行快速排序
        self.quickSort(strs,left,mid-1)

        # 划分之后，再对 mid 右侧的元素进行快速排序
        self.quickSort(strs,mid+1,right)

    # 直接套之前的快速排序的代码进行修改
    # 原先的小于的含义指的是数值上的小于，比如 1  < 10 
    # 但现在的小于含义为：a + b 拼凑的字符串小于 b + a 拼凑的字符串
    # 比如 a = 1 ，b = 10 
    # 那么 a + b = “110”，b + a = “101”
    # 显然，b + a < a + b
    # 也就是说 a 应该放到 b 的后面来拼凑字符串
    def partition( self,strs: List[str] , left : int ,right) -> int : 

        # 经典快速排序的写法
        # 设置当前区间的第一个元素为基准元素
        pivot = strs[left]

        # left 向右移动，right 向左移动，直到 left 和 right 指向同一元素为止
        while left < right : 

            # 当 pivot + strs[right] 的字符串小于 strs[right] + pivot 的字符串时
            # 说明 strs[right] 在正确的位置上，right 向左移动
            # 1  3 
            while  left < right and pivot + strs[right] <=  strs[right] + pivot :
                # right 不断的向左移动
                right -= 1
    

            # 此时，跳出了上面这个 while 循环，说明 pivot + strs[right] 的字符串大于 strs[right] + pivot 的字符串了
            # 说明 strs[right] 不在正确的位置上
            # 将此时的 strs[left] 赋值为 strs[right]
            # 执行完这个操作，比 pivot 小的这个元素被移动到了左侧
            strs[left] = strs[right]

            # 当 strs[left] + pivot 的字符串小于 pivot + strs[left] 的字符串时
            # 说明 strs[left] 在正确的位置上，left 向右移动
            while  left < right and  strs[left] + pivot <= pivot+ strs[left] : 
                # left 不断的向右移动
                left+=1
        

            # 此时，跳出了上面这个 while 循环，说明 strs[left] + pivot 的字符串大于 pivot + strs[left] 的字符串了
            # 说明 strs[left] 不在正确的位置上
            # 将此时的 strs[right] 赋值为 strs[left]
            # 执行完这个操作，比 pivot 大的这个元素被移动到了右侧
            strs[right] = strs[left]

    

        # 此时，left 和 right 相遇，那么需要将此时的元素设置为 pivot
        # 这个时候，pivot 的左侧元素都小于它，右侧元素都大于它
        strs[left] = pivot

        # 返回 left
        return left
'''
# @lc code=end

