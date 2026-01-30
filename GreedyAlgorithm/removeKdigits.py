class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # 用栈，与栈顶元素比较大小，小入，大舍
        s = []
        nums = list(map(int, num))
        print("nums数组:", nums)

        for i in range(len(nums)):
            number = int(nums[i])  # 遍历到的当前元素
            while len(s) != 0 and k > 0 and s[len(s) - 1] > number:
                s.pop(-1)
                k -= 1
            if len(s) != 0 or number != 0:
                s.append(number)

        while len(s) != 0 and k > 0:
            s.pop(-1)
            k -= 1

        result = ""
        result = "".join(str(i) for i in s)
        if result == "":
            return "0"
        return result


if __name__ == '__main__':
    print(Solution().removeKdigits("1432219", 3))
    print(Solution().removeKdigits("10200", 1))
    print(Solution().removeKdigits("10", 2))


