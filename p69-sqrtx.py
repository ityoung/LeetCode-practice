import pytest


class Solution1:
    """
    用矩形面积近似相等得到公式：(同牛顿迭代法)
    假设A为方形面积，Xn+1为计算的方形边长，则有 Xn+1 = 1/2 (Xn + A/Xn)，
    当 (Xn(矩形宽) + A/Xn(矩形长)) / 2 (长与宽的平均值) 中的长宽不断接近，Xn+1与方形边长也越来越接近，
    不断迭代X能更快得到方形边长(A开根)
    """

    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        result = x
        while result > x / result:
            result = (result + x / result) // 2
        return int(result)


class TestCase1(object):
    solution = Solution1()

    @pytest.mark.parametrize('x, result', [
        (4, 2),
        (8, 2),
        (0, 0)
    ])
    def test_mySqrt(self, x, result):
        assert self.solution.mySqrt(x) == result


class Solution2:
    """
    耗时9990+ms, bad solution
    """

    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i = 1
        while i <= x:
            i += 1
            if i ** 2 > x:
                break
        return i - 1


class TestCase2(object):
    solution = Solution2()

    @pytest.mark.parametrize('x, result', [
        (4, 2),
        (8, 2),
        (0, 0)
    ])
    def test_mySqrt(self, x, result):
        assert self.solution.mySqrt(x) == result
