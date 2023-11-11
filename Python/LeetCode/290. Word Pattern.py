class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        size = len(pattern)
        box = dict()
        letters = s.split(" ")

        if size != len(letters):
            return False

        for i in range(size):
            if box.get(pattern[i]):
                if box[pattern[i]] != letters[i]:
                    return False
            else:
                if letters[i] in box.values():
                    return False
                box[pattern[i]] = letters[i]

        return True