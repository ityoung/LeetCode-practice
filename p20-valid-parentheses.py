import pytest


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parenthese_map = {
            '{': '}',
            '[': ']',
            '(': ')'
        }
        stack = []
        while s:
            s0 = s[0]
            if s0 not in parenthese_map:
                if stack and parenthese_map[stack[-1]] == s0:
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(s0)
            s = s[1:]
        if stack:
            return False
        return True


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
