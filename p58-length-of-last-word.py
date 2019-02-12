import pytest


class Solution1:
    """
    48ms, 击败22%
    """
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        slist = s.split()
        last_word = [] if len(slist) == 0 else slist[-1]
        return len(last_word)


class TestCase1(object):
    solution = Solution1()

    @pytest.mark.parametrize('s, result', [
        ('hello world', 5),
        (' ', 0),
        ('  hello  world  ', 5)
    ])
    def test_lengthOfLastWord(self, s, result):
        assert self.solution.lengthOfLastWord(s) == result


class Solution2:
    """
    40ms, 击败99.77%
    """
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        tail = len(s) - 1
        while tail > -1 and s[tail] == ' ':
            tail -= 1
        while tail > -1 and s[tail] != ' ':
            count += 1
            tail -= 1
        return count


class TestCase2(object):
    solution = Solution2()

    @pytest.mark.parametrize('s, result', [
        ('hello world', 5),
        (' ', 0),
        ('  hello  world  ', 5)
    ])
    def test_lengthOfLastWord(self, s, result):
        assert self.solution.lengthOfLastWord(s) == result
