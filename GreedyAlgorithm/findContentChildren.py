from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        child = 0
        cookie = 0
        while child < len(g) and cookie < len(s):
            if g[child] <= s[cookie]:
                child += 1
            cookie += 1
        return child


if __name__ == '__main__':
    print(Solution().findContentChildren([1, 2, 3], [1, 1]))
    print(Solution().findContentChildren([1, 2], [1, 2, 3]))
