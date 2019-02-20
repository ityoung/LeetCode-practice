import pytest

# 将执行记录存在对象之外，当n越大时，递归所依赖的较小的值就都能在result_map中找到，解决了超时问题
result_map = dict()
result_map[1] = 1
result_map[2] = 2


class Solution1:
    """
    搜索公共缓存，减少每个用例间的重复计算
    """

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in result_map:
            return result_map[n]
        else:
            result_map[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return result_map[n]


class TestCase1(object):
    solution = Solution1()

    @pytest.mark.parametrize('n, result', [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5)
    ])
    def test_climbStairs(self, n, result):
        assert self.solution.climbStairs(n) == result


class Solution2:
    """
    动态规划，从小到大记录每次计算结果
    """

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        result_list = [1, 2]
        for i in range(2, n):
            result_list.append(result_list[i - 1] + result_list[i - 2])
        return result_list[n - 1]


class TestCase2(object):
    solution = Solution2()

    @pytest.mark.parametrize('n, result', [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5)
    ])
    def test_climbStairs(self, n, result):
        assert self.solution.climbStairs(n) == result


class Solution3:
    """
    朴素递归，从大到小递归，嵌套层数多，在用例38时超时
    """

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)


class TestCase3(object):
    solution = Solution3()

    @pytest.mark.parametrize('n, result', [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5)
    ])
    def test_climbStairs(self, n, result):
        assert self.solution.climbStairs(n) == result
