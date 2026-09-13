class Solution:
    def arrayPairSum(self, nums):
        nums.sort()

        ans = 0

        for i in range(0, len(nums), 2):
            ans += nums[i]

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna