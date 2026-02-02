from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        # 按起始时间升序，起始时间相同则按结束时间降序排列
        clips.sort(key=lambda x: (x[0], -x[1]))
        print("排序后的数组：", clips)
        n = len(clips)
        current_end = 0
        next_end = 0
        count = 0
        i = 0

        # 当current_end >= time  能用最少的视频拼接出一段完整覆盖范围time的视频
        while current_end < time:
            # 在能衔接的片段中，找到延伸最远的片段
            # clips[i][0]：是片段i的开始时刻
            # # clips[i][1]：是片段i的结束时刻
            while i < n and clips[i][0] <= current_end:
                next_end = max(next_end, clips[i][1])
                i += 1

            #     如果没有找到更远的片段，说明无法覆盖
            if next_end == current_end:
                return -1
            current_end = next_end
            count += 1
        return count


if __name__ == '__main__':
    print(Solution().videoStitching([[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], 10))
    print(Solution().videoStitching([[0,1],[1,2]], 5))
    print(Solution().videoStitching([[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], 9))

