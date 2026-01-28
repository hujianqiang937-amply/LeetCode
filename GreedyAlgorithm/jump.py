from typing import List


# 典型贪心算法，通过局部最优解得到全局最优解
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # max_reach:在当前能到达的范围内，所有位置能跳到的最远值
        # end：当前这一步能到达的最远位置（当前跳跃的边界）
        # step：记录跳跃次数
        max_reach, end, step = 0, 0, 0
        for i in range(n - 1):
            if max_reach >= i:
                max_reach = max(max_reach, nums[i] + i)
                if i == end:
                    end = max_reach
                    step += 1
        return step


if __name__ == '__main__':
    print(Solution().jump([2, 3, 1, 1, 4]))
