import pytest


class Solution:
    """
    能与前一个组成11-19或21-26的情况下+1，其他情况下不加
    """

    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        dp = [1, 1]
        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i - 1] not in ['1', '2']:
                    return 0
                else:
                    dp.append(dp[-2])
            elif s[i - 1] == '1' or (s[i - 1] == '2' and s[i] <= '6'):
                dp.append(dp[-1] + dp[-2])
            else:
                dp.append(dp[-1])
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
