from typing import List

EPS = 1e-9


class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:

        length = len(cards)
        if length == 1:
            return abs(cards[0] - 24) < EPS

        # 4->3->2->1  选两张牌  x=cards[i] 和 y=cards[j]
        for i, x in enumerate(cards):
            for j in range(i + 1, length):
                y = cards[j]

                # 六种情况：加减乘除，其中减法和除法都有两种不同的顺序
                candidates = [x + y, x - y, y - x, x * y]
                if abs(y) > EPS:
                    candidates.append(x / y)
                if abs(x) > EPS:
                    candidates.append(y / x)

                new_cards = cards[:j] + cards[j + 1:]  # 删除j
                for res in candidates:
                    new_cards[i] = res  # 覆盖i
                    if self.judgePoint24(new_cards):
                        return True
        return False


if __name__ == '__main__':
    print(Solution().judgePoint24([4, 1, 8, 7]))
    print(Solution().judgePoint24([1, 2, 1, 2]))
