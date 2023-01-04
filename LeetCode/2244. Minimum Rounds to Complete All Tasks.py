class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """

        memory = dict()

        for i in range(len(tasks)):
            if memory.get(tasks[i]):
                memory[tasks[i]] += 1
            else:
                memory[tasks[i]] = 1

        keys = memory.values()

        answer = 0
        if min(keys) == 1:
            return -1
        else:
            for num in keys:
                if num < 4:
                    answer += 1
                else:
                    if not (num % 3):
                        answer += num // 3
                    else:
                        three = num // 3
                        while True:
                            if not ((num - 3 * three) % 2):
                                answer += three + (num - 3 * three) // 2
                                break
                            three -= 1

                    # 빠른 사람들은 num % 3 의 값으로 2의 값을 판별
                    # 0(3으로만 구성)
                    # 1(총 n개중 3이 n-2개 2가 2개)
                    # 2(총 n개중 3이 n-1개 2가 1개)

        return answer


now = Solution()
print(now.minimumRounds([2,3,3]))
