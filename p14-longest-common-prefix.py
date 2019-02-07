import pytest


class Solution:
    def longestCommonPrefix(self, strs: list):
        """
        :type strs: List[str]
        :rtype: str
        """
        length = len(strs)
        if length == 1:
            return strs[0]

        strs.sort(key=lambda i: len(i), reverse=False)
        i = 0
        result = ""
        while i < length - 1:
            result = ""
            for index, c in enumerate(strs[i]):
                if c == strs[i + 1][index]:
                    result += c
                else:
                    break
            strs[i + 1] = result
            i += 1
        return result


class TestCases(object):
    solution = Solution()

    @pytest.mark.parametrize('strs, result', [
        (['flow'], 'flow'),
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["aaa", "aa", "aaa"], "aa")
    ])
    def test_longestCommonPrefix(self, strs, result):
        assert self.solution.longestCommonPrefix(strs) == result
