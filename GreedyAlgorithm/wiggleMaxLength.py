from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        BEGIN = 0
        UP = 1
        DOWN = 2
        STATE = BEGIN
        vision = [BEGIN, UP, DOWN]
        max_length = 1
        for i in range(1, len(nums)):
            if STATE == 0:
                if nums[i - 1] > nums[i]:
                    STATE = 2
                    max_length += 1
                elif nums[i - 1] < nums[i]:
                    STATE = 1
                    max_length += 1
            if STATE == 1:
                if nums[i - 1] > nums[i]:
                    STATE = 2
                    max_length += 1
            if STATE == 2:
                if nums[i - 1] < nums[i]:
                    STATE = 1
                    max_length += 1
        return max_length


if __name__ == '__main__':
    print(Solution().wiggleMaxLength([1,7,4,9,2,5]))
    print(Solution().wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]))
    print(Solution().wiggleMaxLength([1, 2, 3, 4, 5, 6, 7, 8, 9]))



