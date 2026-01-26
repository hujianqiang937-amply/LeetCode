class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        return self.fib(n - 1) + self.fib(n - 2)


if __name__ == '__main__':
    print(Solution().fib(2))
    print(Solution().fib(3))
    print(Solution().fib(4))
