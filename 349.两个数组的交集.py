#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        length1,length2=len(nums1),len(nums2)

        res=list()
        index,index1,index2=0,0,0 #三指针，两个list，返回的list

        while index1<length1 and index2<length2:
            num1=nums1[index1]
            num2=nums2[index2]

            if num1==num2:
                # 不是头，也不和上一个元素重复
                if not res or num1!=res[-1]:
                    res.append(num1)
            
                index1+=1
                index2+=1
            elif num1<num2:
                index1+=1
            else:
                index2+=1
        return res
'''
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 首先对两个数组进行排序
        nums1.sort()

        nums2.sort()

        # 计算出两个数组的长度
        length1 = len(nums1)
        
        length2 = len(nums2)

        # 两个数组的交集结果数组长度必然是小于等于最短数组的长度
        res = list()

        # 设置三个索引指针

        # index 指向结果数组 res ，每当 index 指向的位置填充了元素就向后移动
        # index = 0
        
        # index1 指向数组 nums1 中的元素，将该元素和 index2 指向数组 nums2 中的元素进行比较
        index1 = 0
        
        # index2 指向数组 nums2 中的元素，将该元素和 index1 指向数组 nums1 中的元素进行比较
        index2 = 0

        # 移动 index1 和 index2 
        while index1 < length1 and index2 < length2 :
            
            # 获取 index1 指向的元素值
            num1 = nums1[index1]
            
            # 获取 index2 指向的元素值
            num2 = nums2[index2]

            # num1 和 num2 的大小关系有三种

            # 1、num1 == num2
            if num1 == num2 :

                # 由于输出结果中的每个元素一定是 【唯一】 的，所以要做一下判断
                # 如果 res 中的 index 在起始位置，说明还没有存放元素
                # 那么这个相等的元素可以存放到 res 中

                # 如果 res 中的 index 不在起始位置
                # 当它前面存放的元素并不是现在想要存放的元素
                # 那么这个相等的元素可以存放到 res 中
                if not res or num1 != res[-1]:
                    res.append(num1)

                # 移动 index1 ，比较其它元素
                index1 += 1
                # 移动 index2 ，比较其它元素
                index2 += 1

            # 2、num1 < num2
            elif num1 < num2 :
                
                # 由于两个数组已经排序了，说明此时 num1 肯定会小于 nums2 数组中 num2 后面所有的数
                # 那 num1 肯定是无法在 nums2 中找到相等的元素
                # 移动 index1 ，比较其它元素
                index1 += 1

            # 3、num1 > num2
            else:

                # 由于两个数组已经排序了，说明此时 num2 肯定会小于 nums1 数组中 num1 后面所有的数
                # 那 num2 肯定是无法在 nums1 中找到相等的元素
                # 移动 index2 ，比较其它元素
                index2 += 1

        # 最后返回结果数组中有值的那些元素就行
        return res
'''
# @lc code=end

