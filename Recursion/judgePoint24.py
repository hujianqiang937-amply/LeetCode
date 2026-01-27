EPS = 1e-9  # 浮点数误差阈值


class Solution:
    def judgePoint24(self, cards: list[int]) -> bool:
        length = len(cards)
        # 递归结束条件：只剩1个数时，判断是否近似等于24
        if length == 1:
            return abs(cards[0] - 24) < EPS

        # 分治：选两个数x和y,做所有可能运算
        for i, x in enumerate(cards):
            for j in range(i + 1, length):  # j>i,避免重复选
                y = cards[j]

                # 6种运算情况：加、减（x-y和y-x）、乘、除（x/y和y/x）
                candidates = [x + y, x * y]
                candidates.append(x - y)
                candidates.append((y - x))
                if (abs(y) > EPS):
                    candidates.append(x / y)
                if (abs(x) > EPS):
                    candidates.append(y / x)

                    # 生成新列表：去掉x和y，加入运算结果
                    new_cards = cards[:i] + cards[i + 1:j] + cards[j + 1:]  # 先去掉i和j位置的数
                    for res in candidates:
                        if self.judgePoint24(new_cards + [res]):
                            return True

        # 所有情况都试完，无法得到24
        return False


if __name__ == '__main__':
    print(Solution().judgePoint24([4, 1, 8, 7]))
    print(Solution().judgePoint24([1, 2, 1, 2]))
