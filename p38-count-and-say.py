import pytest


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # 奇数：尾数为1；偶数：尾数为11
        # tail = '1' if n % 1 else '11'
        if n == 1:
            return '1'
        string = "1"
        for i in range(n - 1):
            si = 0
            counter = 1
            slength = len(string)
            new_string = ''
            while si < slength:
                char = string[si]
                si += 1
                while si < slength and string[si] == char:
                    si += 1
                    counter += 1
                else:
                    new_string = '{}{}{}'.format(new_string, counter, char)
                    counter = 1
            string = new_string
        return string


class TestCase(object):
    solution = Solution()

    @pytest.mark.parametrize('n, result', [
        (1, '1'),
        (2, '11'),
        (4, '1211'),
        (6, '312211'),
    ])
    def test_countAndSay(self, n, result):
        assert self.solution.countAndSay(n) == result
