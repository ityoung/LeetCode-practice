import pytest


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_length = len(s)
        dp = [[0 for _ in range(str_length)] for _ in range(str_length)]
        longest_sub_str = ""
        # 从最小长度的子串开始，生成回文子串的矩阵表，较大长度的子串依赖较小长度子串的回文情况
        for length in range(str_length):
            for left in range(str_length - length):
                right = left + length
                if s[left] == s[right]:
                    # 长度为1和2时，本身已经是最小的子串单位
                    # 长度大于2时，则判断去头去尾的子串是否为回文串
                    if length < 2 or dp[left + 1][right - 1] == 1:
                        dp[left][right] = 1
                        longest_sub_str = s[left:right + 1]
        return longest_sub_str


class TestCase(object):
    solution = Solution()

    @pytest.mark.parametrize('s, result', [
        ('babad', 'aba'),
        ('cbbd', 'bb')
    ])
    def test_longestPalindrome(self, s, result):
        assert self.solution.longestPalindrome(s) == result
