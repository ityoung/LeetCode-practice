from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """自底向上，相邻取小+当前值，最后第一位为结果"""
        record = triangle[-1].copy()
        t_len = len(triangle)
        for row_offset in range(1, t_len):
            calc_row = t_len - row_offset
            for col in range(calc_row):
                record[col] = min(record[col], record[col + 1]) + triangle[calc_row-1][col]
        return record[0]


if __name__ == '__main__':
    s = Solution()
    r = s.minimumTotal([
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ])
    print(r)
