import pytest


# TODO: This solution is cheat with built-in method
class Solution1:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)


class TestCase1(object):
    solution = Solution1()

    @pytest.mark.parametrize('haystack, needle, result', [
        ('hello', 'll', 2),
        ('hello', 'lo', 3),
        ('aaaaa', 'bba', -1),
        ('aaaaa', '', 0),
    ])
    def test_strStr(self, haystack, needle, result):
        assert self.solution.strStr(haystack, needle) == result
