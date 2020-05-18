from typing import List

class Solution:
    def _rec(self, n, left_used, right_used):
        if left_used < right_used or right_used == n:
            return []
        elif left_used == n:
            return [')' * (left_used-right_used)]
        result = []
        left_res = self._rec(n, left_used+1, right_used)
        [result.append('('+lr) for lr in left_res]
        right_res = self._rec(n, left_used, right_used+1)
        [result.append(')'+rr) for rr in right_res]
        return result

    def generateParenthesis(self, n: int) -> List[str]:
        res = self._rec(n, 1, 0)
        return ['('+ r for r in res]

if __name__ == '__main__':
    s = Solution()
    r = s.generateParenthesis(3)
    print(r)