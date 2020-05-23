class Solution:
    def climbStairs(self, n: int) -> int:
        # f(n) = f(n-1)+f(n-2)
        f = [1, 2]
        for i in range(2, n):
            f.append(f[i - 1] + f[i - 2])
        return f[n - 1]


if __name__ == '__main__':
    s = Solution()
    r = s.climbStairs(3)
    print(r)
