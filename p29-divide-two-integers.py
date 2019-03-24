import pytest

MIN_INT = -2 ** 31
MAX_INT = 2 ** 31 - 1


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negative = False
        if (dividend ^ divisor) < 0:
            negative = True
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0
        for i in range(31, -1, -1):
            if divisor > dividend:
                break
            if 2 ** i * divisor <= dividend:
                result += 2 ** i
                dividend = dividend - 2 ** i * divisor
        result = -result if negative else result
        if result < MIN_INT or result > MAX_INT:
            return MAX_INT
        return result


class Solution2:
    """
    TODO: 将解法1改为移位运算
    解题思路：这题是除法，所以先普及下除法术语
    商，公式是：(被除数-余数)÷除数=商，记作：被除数÷除数=商...余数，是一种数学术语。
    在一个除法算式里，被除数、余数、除数和商的关系为：(被除数-余数)÷除数=商，记作：被除数÷除数=商...余数，
    进而推导得出：商×除数+余数=被除数。
    要求商，我们首先想到的是减法，能被减多少次，那么商就为多少，但是明显减法的效率太低
    那么我们可以用位移法，因为计算机在做位移时效率特别高，向左移1相当于乘以2，向右位移1相当于除以2
    我们可以把一个dividend（被除数）先除以2^n，n最初为31，不断减小n去试探,当某个n满足dividend/2^n>=divisor时，
    表示我们找到了一个足够大的数，这个数*divisor是不大于dividend的，所以我们就可以减去2^n个divisor，以此类推
    我们可以以100/3为例
    2^n是1，2，4，8...2^31这种数，当n为31时，这个数特别大，100/2^n是一个很小的数，肯定是小于3的，所以循环下来，
    当n=5时，100/32=3, 刚好是大于等于3的，这时我们将100-32*3=4，也就是减去了32个3，接下来我们再处理4，同样手法可以再减去一个3
    所以一共是减去了33个3，所以商就是33
    这其中得处理一些特殊的数，比如divisor是不能为0的，Integer.MIN_VALUE和Integer.MAX_VALUE
    移位针对除数为2的情况为：x / 2 = x >> 1, x / (2^n) = x >> n
    """


class TestCase(object):
    solution = Solution()

    @pytest.mark.parametrize('dividend, divisor, result', [
        (-2 ** 31, -1, 2 ** 31 - 1),
        (2 ** 33, 3, 2 ** 31 - 1),
        (10, 3, 3),
        (7, -3, -2)
    ])
    def test_divide(self, dividend: int, divisor: int, result: int):
        assert self.solution.divide(dividend, divisor) == result
