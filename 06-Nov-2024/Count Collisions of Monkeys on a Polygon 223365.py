# Problem: Count Collisions of Monkeys on a Polygon - https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/

class Solution:
    def monkeyMove(self, n: int) -> int:
        return (pow(2, n, 10 ** 9 + 7) - 2) % (10 ** 9 + 7)