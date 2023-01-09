# Wrong

class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:

        points.sort()
        need_arrow = 1
        start = 0
        now = 1

        while start + now < len(points):
            if points[start + now][0] > points[start][1]:
                need_arrow += 1
                start += now
                now = 1

            else:
                now += 1

        return need_arrow


solution = Solution()
print(solution.findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]))
