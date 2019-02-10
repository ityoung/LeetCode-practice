import pytest


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


class Solution2:
    """
    暴力解法
    """
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        nindex = index = 0
        length = len(haystack)
        nlength = len(needle)
        while index < length and nindex < nlength:
            if haystack[index] == needle[nindex]:
                index += 1
                nindex += 1
            else:
                index = index - nindex + 1
                nindex = 0
        if nindex == nlength:
            return index - nindex
        return -1


class TestCase2(object):
    solution = Solution2()

    @pytest.mark.parametrize('haystack, needle, result', [
        ('hello', 'll', 2),
        ('hello', 'lo', 3),
        ('aaaaa', 'bba', -1),
        ('aaaaa', '', 0),
    ])
    def test_strStr(self, haystack, needle, result):
        assert self.solution.strStr(haystack, needle) == result


class Solution3:
    """
    TODO: KMP
    """
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """


# class TestCase3(object):
#     solution = Solution3()
#
#     @pytest.mark.parametrize('haystack, needle, result', [
#         ('hello', 'll', 2),
#         ('hello', 'lo', 3),
#         ('aaaaa', 'bba', -1),
#         ('aaaaa', '', 0),
#     ])
#     def test_strStr(self, haystack, needle, result):
#         assert self.solution.strStr(haystack, needle) == result
