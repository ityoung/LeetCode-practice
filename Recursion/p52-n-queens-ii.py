class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count = 0

        def oneQueen(row, cols, diffs, sums):
            if len(cols) < row:
                return
            if row == n:
                self.count += 1
                return
            for i in range(n):
                if i in cols or (i + row) in diffs or (i - row) in sums:
                    continue
                oneQueen(row + 1, cols + [i], diffs + [i + row], sums + [i - row])

        oneQueen(0, [], [], [])
        return self.count


if __name__ == '__main__':
    s = Solution()
    r = s.totalNQueens(8)
    print(r)
