class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        s_len = len(p)
        sort_p = "".join(sorted(p))
        result = []

        for i in range(len(s) - s_len + 1):
            if "".join(sorted(s[i: i + s_len])) == sort_p:
                result.append(i)

        return result

solution = Solution().findAnagrams("abab", "ab")
print(solution)