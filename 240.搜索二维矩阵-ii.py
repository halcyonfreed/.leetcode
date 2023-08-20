#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i,j=len(matrix)-1,0
        while i>=0 and j<len(matrix[0]):
            if matrix[i][j]<target:
                j+=1
            elif matrix[i][j]>target:
                i-=1
            else:
                return True
        return False

'''
// 登录 AlgoMooc 官网获取更多算法图解
// https://www.algomooc.com
// 作者：程序员吴师兄
// 添加微信 278166530 获取最新课程
// 代码有看不懂的地方一定要私聊咨询吴师兄呀
// LeetCode 240、搜索二维矩阵 II：https://leetcode.cn/problems/search-a-2d-matrix-ii/submissions/
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {

        // 从数组的最左下角位置开始去搜索整个二维数组
        // 1、当发现当前遍历的元素大于 target 时，意味着这个元素后面的所有元素也都大于 target
        // 那么就不用去搜索这一行了
        // 2、当发现当前遍历的元素小于 target 时，意味着这个元素上面的所有元素也都小于 target
        // 那么就不用去搜索这一列了

        // 初始化 i 和 j 为数组左下角元素
        // 最后一行
        int i = matrix.length - 1;

        // 第 0 列
        int j = 0;

        // 从数组的左下角开始出发，只要 i 和 j 没有越界继续判断
        while( i >= 0 && j <= matrix[0].length - 1 ){
            
            // 当发现当前遍历的元素大于 target 时，意味着这个元素后面的所有元素也都大于 target
            if(matrix[i][j] > target){

                // 行索引向上移动一格（即 i-- ），即消去矩阵第 i 行元素
                i--;
            
            // 当发现当前遍历的元素小于 target 时，意味着这个元素上面的所有元素也都小于 target
            }else if(matrix[i][j] < target){

                // 列索引向右移动一格（即 j++ ），即消去矩阵第 j 列元素
                j++;

            // 否则，说明找到目标值
            }else{

                // 直接返回 ture
                return true;
            }     
        }

        // 遍历了整个二维数组，没有找到目标值，返回 false
        return false;
    }
}
'''
# @lc code=end

