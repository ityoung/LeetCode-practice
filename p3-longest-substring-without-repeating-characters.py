import pytest


# 这是LeetCode官方给出的基础模版, 我们在这模版上完成功能
class Solution1(object):
    """
    O(n^3)
    """

    def is_unique(self, s: str) -> bool:
        """
        判断 s 中的字符均为唯一
        :param s:
        :return:
        """
        char_set = set()
        for c in s:
            if c in char_set:
                # 字符已经存在, 该字符串中的字符不唯一
                return False
            char_set.add(c)
        return True

    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length < 2:
            return length
        ans = 1
        for i in range(0, length - 1):
            for j in range(i + 1, length):
                if not self.is_unique(s[i:j + 1]):
                    # 字符串中有重复的字符, 不符合条件, 不需要继续
                    break
                sub_len = j - i + 1
                ans = sub_len if sub_len > ans else ans
        return ans


class TestCases1(object):
    # 初始化一个类对象
    solution = Solution1()

    '''
    输入: "abcabcbb"
    输出: 3

    输入: "bbbbb"
    输出: 1

    输入: "pwwkew"
    输出: 3

    输入: ""
    输出: 0

    输入: "a"
    输出: 1

    输入: "au"
    输出: 2
    '''

    # 添加参数化执行测试用例模版
    @pytest.mark.parametrize('s, length', [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("a", 1),
        ("au", 2),
    ])
    def test_solution(self, s: str, length: int):
        assert self.solution.lengthOfLongestSubstring(s) == length

    @pytest.mark.parametrize('s, result', [
        ('aa', False),
        ('a', True)
    ])
    def test_is_unique(self, s: str, result: bool):
        assert self.solution.is_unique(s) == result


class Solution2(object):

    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length < 2:
            return length
        ans = 1
        for i in range(0, length - 1):
            for j in range(i + 1, length):
                if s[j] in s[i:j]:
                    break
                sub_len = j - i + 1
                ans = sub_len if sub_len > ans else ans
        return ans


class TestCases2(object):
    solution = Solution2()

    '''
    输入: "abcabcbb"
    输出: 3

    输入: "bbbbb"
    输出: 1

    输入: "pwwkew"
    输出: 3

    输入: ""
    输出: 0

    输入: "a"
    输出: 1

    输入: "au"
    输出: 2
    '''

    @pytest.mark.parametrize('s, length', [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("a", 1),
        ("au", 2),
    ])
    def test_solution(self, s: str, length: int):
        assert self.solution.lengthOfLongestSubstring(s) == length


class Solution3(object):

    def get_index(self, s: str, c: str):
        """

        :param s: string
        :param c: character
        :return: index of c in s, or None
        """
        length = len(s)
        for index in range(0, length):
            if s[index] == c:
                return index
        return None

    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length < 2:
            return length
        ans = 1
        i = 0
        find_flag = False
        # for i in range(0, length - 1):
        while i < length:
            for j in range(i + 1, length):
                index = self.get_index(s[i:j], s[j])
                if index is not None:
                    i += index + 1
                    find_flag = True
                    break
                sub_len = j - i + 1
                ans = sub_len if sub_len > ans else ans
            if find_flag:
                find_flag = False
                continue
            i+=1
        return ans


class TestCases3(object):
    solution = Solution3()

    '''
    输入: "abcabcbb"
    输出: 3

    输入: "bbbbb"
    输出: 1

    输入: "pwwkew"
    输出: 3

    输入: ""
    输出: 0

    输入: "a"
    输出: 1

    输入: "au"
    输出: 2

    输入: "aab"
    输出: 2
    '''

    @pytest.mark.parametrize('s, length', [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("a", 1),
        ("au", 2),
        ("aab", 2),
    ])
    def test_solution(self, s: str, length: int):
        assert self.solution.lengthOfLongestSubstring(s) == length

    @pytest.mark.parametrize('s, c, result', [
        ('abc', 'b', 1),
        ('a', 'b', None)
    ])
    def test_is_unique(self, s: str, c: str, result):
        assert self.solution.get_index(s, c) == result

if __name__ == '__main__':
    solution = Solution3()
    print(solution.lengthOfLongestSubstring('aab'))
