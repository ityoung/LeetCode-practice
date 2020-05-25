from typing import List


class UnionFind:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        # 定义一维数组，loc = now_row * col + now_col
        # self.parent = [i for i in range(m * n)]
        self.parent = [-1] * (m * n)
        self.rank = [0] * (m * n)
        self.count = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1':
                    self.parent[row * n + col] = row * n + col
                    self.count += 1

    def find(self, i):
        """查找root"""
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, l, u):
        root_left = self.find(l)
        root_up = self.find(u)
        if root_left == root_up:
            return
        if self.rank[root_left] < self.rank[root_up]:
            self.parent[root_left] = root_up
        elif self.rank[root_left] > self.rank[root_up]:
            self.parent[root_up] = root_left
        else:
            self.parent[root_left] = root_up
            self.rank[root_up] += 1
        self.count -= 1


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        uf = UnionFind(grid)
        # 节点本身对应的四个方向
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for row in range(m):
            for col in range(n):
                if grid[row][col] == '0':
                    continue
                for d in directions:
                    cmp_row, cmp_col = row + d[0], col + d[1]
                    if 0 <= cmp_row < m and 0 <= cmp_col < n and grid[cmp_row][cmp_col] == '1':
                        uf.union(row * n + col, cmp_row * n + cmp_col)
        return uf.count


if __name__ == '__main__':
    s = Solution()
    r = s.numIslands(
        [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]])
    assert r == 1
