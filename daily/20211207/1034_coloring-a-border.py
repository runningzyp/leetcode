"""
给你一个大小为 m x n 的整数矩阵 grid ，表示一个网格。另给你三个整数 row、col 和 color 。网格中的每个值表示该位置处的网格块的颜色。

两个网格块属于同一 连通分量 需满足下述全部条件：

两个网格块颜色相同
在上、下、左、右任意一个方向上相邻
连通分量的边界 是指连通分量中满足下述条件之一的所有网格块：

在上、下、左、右四个方向上与不属于同一连通分量的网格块相邻
在网格的边界上（第一行/列或最后一行/列）
请你使用指定颜色 color 为所有包含网格块 grid[row][col] 的 连通分量的边界 进行着色，并返回最终的网格 grid 。

 

示例 1：

输入：grid = [[1,1],[1,2]], row = 0, col = 0, color = 3
输出：[[3,3],[3,2]]
示例 2：

输入：grid = [[1,2,2],[2,3,2]], row = 0, col = 1, color = 3
输出：[[1,3,3],[2,3,3]]
示例 3：

输入：grid = [[1,1,1],[1,1,1],[1,1,1]], row = 1, col = 1, color = 2
输出：[[2,2,2],[2,1,2],[2,2,2]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coloring-a-border
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Cell:
    def __init__(self, x, y, value, row, col) -> None:
        self.x = x
        self.y = y
        self.value = value
        self.is_board = False  # 是否联通份量
        if self.x == 0 or self.y == 0 or self.x == row or self.y == col:
            self.is_edge = True
        else:
            self.is_edge = False
        self.is_vistor = False

    def up(self, maps):
        up_cell = maps.get((self.x - 1, self.y))
        if up_cell and up_cell.value == self.value:
            if up_cell.is_vistor:
                return False
            return up_cell.start(maps)
        return True

    def down(self, maps):
        down_cell = maps.get((self.x + 1, self.y))
        if down_cell and down_cell.value == self.value:
            if down_cell.is_vistor:
                return False
            return down_cell.start(maps)
        return True

    def left(self, maps):
        left_cell = maps.get((self.x, self.y - 1))
        if left_cell and left_cell.value == self.value:
            if left_cell.is_vistor:
                return False
            return left_cell.start(maps)
        return True

    def right(self, maps):
        right_cell = maps.get((self.x, self.y + 1))
        if right_cell and right_cell.value == self.value:
            if right_cell.is_vistor:
                return False
            return right_cell.start(maps)
        return True

    def start(self, maps):
        self.is_vistor = True
        if any([self.up(maps), self.down(maps), self.left(maps), self.right(maps)]):
            self.is_board = True
        return False

    def __str__(self):
        return str(
            (self.x, self.y, " is_edge: ", self.is_edge, " is_board: ", self.is_board)
        )

    __repr__ = __str__


class Solution:
    def colorBorder(
        self, grid: List[List[int]], row: int, col: int, color: int
    ) -> List[List[int]]:
        width = len(grid[0]) - 1
        height = len(grid) - 1
        cells = dict()
        for x, rows in enumerate(grid):
            for y, value in enumerate(rows):
                cells[(x, y)] = Cell(x, y, value, height, width)
        cell = cells.get((row, col))
        cell.start(cells)
        result = []
        for x, rows in enumerate(grid):
            result_line = []
            for y, value in enumerate(rows):
                cell = cells.get((x, y))
                if cell.is_board:
                    result_line.append(color)
                else:
                    result_line.append(cell.value)
            result.append(result_line)
        return result


if __name__ == "__main__":
    assert Solution().colorBorder(
        grid=[[1, 2, 2], [2, 3, 2]], row=0, col=1, color=3
    ) == [[1, 3, 3], [2, 3, 3]]
    assert Solution().colorBorder(
        grid=[[1, 1, 1], [1, 1, 1], [1, 1, 1]], row=1, col=1, color=2
    ) == [[2, 2, 2], [2, 1, 2], [2, 2, 2]]
