class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        index = 0
        checked = []
        success = 0

        def dfs(now):
            nonlocal checked, success
            if now in checked or success:
                return

            if now == len(nums) - 1:
                success = 1
                return

            for i in range(nums[now], 0, -1):
                dfs(now + i)
                checked.append(now + i)

        dfs(index)
        return True if success else False


a = Solution()
print("true") if a.canJump([2,3,1,1,4]) else print("false")
