import pytest


class Solution:
    """
    能与前一个组成11-19或21-26的情况下+1，其他情况下不加
    """

    def numDecodings(self, s: str) -> int:
        length = len(s)
        if length == 0 or (length > 0 and s[0] == '0'):
            return 0
        if length == 1:
            return 1
        dp = [1] * len(s)
        if s[1] == '0':
            if s[0] not in ['1', '2']:
                return 0
        elif int(s[:2]) <= 26:
            dp[1] = 2
        for i in range(2, length):
            if s[i] == '0':
                if s[i - 1] not in ['1', '2']:
                    return 0
                else:
                    dp[i] = dp[i - 2]
            elif s[i - 1] == '1' or (s[i - 1] == '2' and int(s[i]) <= 6):
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]
        return dp[-1]


class TestCase:
    solution = Solution()

    @pytest.mark.parametrize('s, result', [
        ("12", 2),
        ("226", 3),
        ("1027", 1),
        ("22222", 8),
        ("90", 0),
        ("100", 0),
        ("01", 0),
        ("0", 0),
        ("110", 1),
    ])
    def test_numDecodings(self, s: str, result: int):
        assert self.solution.numDecodings(s) == result
