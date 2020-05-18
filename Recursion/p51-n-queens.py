from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def _oneQueen(row, cols, diffs, sums):
            # 终止条件
            if len(cols) < row:
                return
            if row == n:
                result.append(cols)
                return cols
            # 递归
            for col in range(n):
                if col in cols or (col + row) in diffs or (col - row) in sums:
                    continue
                _oneQueen(row + 1, cols + [col], diffs + [col + row], sums + [col - row])

        result = []
        _oneQueen(0, [], [], [])
        # [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
        all_solve = []
        for queens in result:
            one_solve = []
            for q in queens:
                lines = ""
                for i in range(n):
                    if i == q:
                        lines += "Q"
                    else:
                        lines += "."
                one_solve.append(lines)
            all_solve.append(one_solve)
        return all_solve
        # return [["" for q in queens] for queens in result]


if __name__ == '__main__':
    s = Solution()
    r = s.solveNQueens(1)
    print(r)
