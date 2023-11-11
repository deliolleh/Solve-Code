class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # While numRows 1, there is no zigzag => return s
        if numRows == 1:
            return s

        # Array for zigzag, length of array is numRows
        zigzags = [""] * numRows
        # index of s
        now = 0
        # index of zigzags
        row = 0
        # select next step
        types = 1
        while now < len(s):
            zigzags[row] += s[now]
            now += 1

            # straight type
            if types:
               row += 1
               if row == numRows - 1:
                   types = 0

            # diagonal type
            else:
                row -= 1
                if row == 0:
                    types = 1

        # connect all array
        return ''.join(zigzags)

solution = Solution().convert("PAYPALISHIRING", 4)
print(solution)
