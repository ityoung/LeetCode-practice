import pytest


class Solution:
    def isValid(self, s: str) -> bool:
        pair_map = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        stack = []
        for c in s:
            if c in ["{", "[", "("]:
                stack.append(c)
            elif c in ["}", "]", ")"] and stack and stack[-1] == pair_map[c]:
                stack.pop()
            else:
                return False
        return stack == []


class TestCases(object):
    solution = Solution()

    @pytest.mark.parametrize('s, result', [
        ("", True),
        ('{}', True),
        ('{]', False),
        ('{}[]()', True),
        ('([)]', False),
        ('{()}', True),
        ('}{', False)
    ])
    def test_isValid(self, s, result):
        assert self.solution.isValid(s) == result
