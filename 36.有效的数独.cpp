/*
 * @lc app=leetcode.cn id=36 lang=cpp
 *
 * [36] 有效的数独
 */

// @lc code=start
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {

    }
};

/*

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {

        // 使用哈希表记录每一行每个数字出现的次数
        // 由于数字是从 1 - 9 ，因此可以采取数组的形式来表示哈希表
        // 即利用数组的索引作为哈希表的 key ， 数组的元素值作为哈希表的 value
        int rows[9][9];
        memset(rows,0,sizeof(rows));

        // 使用哈希表记录每一列每个数字出现的次数
        // 由于数字是从 1 - 9 ，因此可以采取数组的形式来表示哈希表
        // 即利用数组的索引作为哈希表的 key ， 数组的元素值作为哈希表的 value
        int columns[9][9];
        memset(columns,0,sizeof(columns));
        // 使用哈希表记录每一个【小九宫格】每个数字出现的次数
        // 由于数字是从 1 - 9 ，因此可以采取数组的形式来表示哈希表
        // 即利用数组的索引作为哈希表的 key ， 数组的元素值作为哈希表的 value
        int subboxes[3][3][9];
        memset(subboxes,0,sizeof(subboxes));
        // 一行行一列列去访问二维矩阵 board 的每个元素
        for (int i = 0 ; i < 9 ; i++) {

            for (int j = 0 ; j < 9 ; j++) {
                
                // 获取当前小方格的字符
                char c = board[i][j];

                // 如果不是空白格而是数字
                if (c != '.') {
                    
                    // 由于数组的索引是从 0 开始的，而小方格的值是从 1 开始的
                    // 因此，索引 0 代表 key 为 1
                    // 索引 1 代表 key 为 2
                    // 所以，c 为 9 时，存储在索引为 8 的位置
                    // c 为 6 时，存储在索引为 5 的位置
                    int index = c - '0' - 1;

                    // 第 i 行数字 index 出现的次数增加 1 次
                    rows[i][index]++;
                    
                    // 第 j 列数字 index 出现的次数增加 1 次
                    columns[j][index]++;

                    // 总共有 9 个 3 * 3 的小九宫格
                    // 第一行有 3 个，包含了第 0 个、第 1 个、第 2 个
                    // 第二行有 3 个，包含了第 3 个、第 4 个、第 5 个
                    // 第三行有 3 个，包含了第 6 个、第 7 个、第 8 个
                    // (i / 3 , j / 3) 表示是第几个小九宫格
                    // 当前这个小九宫格里面数字 index 出现的次数增加 1 次
                    subboxes[ i  / 3 ][j  / 3 ][index]++;

                    // 如果发现如下任何一种情况，都说明是无效的
                    // 1、这一行统计出 index 数字的次数大于 1 个
                    // 2、这一列统计出 index 数字的次数大于 1 个
                    // 3、这一小九宫格统计出 index 数字的次数大于 1 个
                    if (rows[i][index] > 1 || columns[j][index] > 1 || subboxes[i/3][j/3][index] > 1) {             
                        // 返回 false
                        return false;
                    }
                }
            }
        }

        // 是有效的，返回 true
        return true;

    }
};
*/
// @lc code=end

