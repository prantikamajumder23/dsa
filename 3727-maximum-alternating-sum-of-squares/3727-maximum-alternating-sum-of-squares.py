class Solution(object):
    def maxAlternatingSum(self, nums):
        nums.sort(key=lambda x: x * x)

        n = len(nums)
        ans = 0

        for i in range(n):
            if i < n // 2:
                ans -= nums[i] * nums[i]
            else:
                ans += nums[i] * nums[i]

        return ans


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna