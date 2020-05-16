class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 二分相乘
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1 / x
        half = self.myPow(x, n // 2)
        return half * half if n % 2 == 0 else half * half * x


if __name__ == '__main__':
    s = Solution()
    r1 = s.myPow(2.00000, 10)
    assert r1 == 1024.00000
