class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        alien_order = dict()
        for i in range(len(order)):
            alien_order[order[i]] = i + 1

        for j in range(len(words) - 1):
            forward = words[j]
            behind = words[j + 1]
            length = min(len(forward), len(behind))

            for l in range(length):
                f_word = forward[l]
                b_word = behind[l]
                if alien_order[f_word] < alien_order[b_word]:
                    break
                elif alien_order[f_word] > alien_order[b_word]:
                    return False
            else:
                if len(forward) > len(behind):
                    return False
        return True


solution = Solution()
print('true') if solution.isAlienSorted(
    ["hello", "leetcode"],
    "hlabcdefgijkmnopqrstuvwxyz") else print('false')
