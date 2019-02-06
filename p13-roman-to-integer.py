import pytest


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        value_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        for i in range(len(s) - 1):
            left = value_map[s[i]]
            if left < value_map[s[i+1]]:
                result -= left
            else:
                result += left
        return result + value_map[s[-1]]


class TestCases(object):
    solution = Solution()

    @pytest.mark.parametrize('s, result', [
        ("III", 3),
        ("IV", 4),
        ("IX", 9),
        ("LVIII", 58),
        ("MCMXCIV", 1994)
    ])
    def test_romanToInt(self, s: str, result: int):
        assert self.solution.romanToInt(s) == result
