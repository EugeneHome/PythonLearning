# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#  
# 
#  示例 2： 
#  
#  
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 10 
#  -100 <= matrix[i][j] <= 100 
#  
# 
#  Related Topics 数组 矩阵 模拟 👍 1891 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.row_num = None

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row_num = len(matrix)
        col_num = len(matrix[0])
        ans = []
        pos = [0, -1]
        direction = 0
        move = [self.right, self.down, self.left, self.up]
        while len(ans) < row_num * col_num:
            move[direction % 4](pos)
            if not (0 <= pos[0] < row_num and 0 <= pos[1] < col_num and matrix[pos[0]][pos[1]] is not None):
                move[(direction + 2) % 4](pos)
                direction += 1
                move[direction % 4](pos)
            ans.append(matrix[pos[0]][pos[1]])
            matrix[pos[0]][pos[1]] = None
        return ans

    @staticmethod
    def left(pos):
        pos[1] -= 1

    @staticmethod
    def right(pos):
        pos[1] += 1

    @staticmethod
    def up(pos):
        pos[0] -= 1

    @staticmethod
    def down(pos):
        pos[0] += 1
# leetcode submit region end(Prohibit modification and deletion)
