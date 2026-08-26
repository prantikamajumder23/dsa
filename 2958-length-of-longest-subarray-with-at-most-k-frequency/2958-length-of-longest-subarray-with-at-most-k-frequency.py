class Solution(object):
    def maxSubarrayLength(self, nums, k):
     freq = {}
     left = 0
     max_length = 0

     for right in range(len(nums)):

        freq[nums[right]] = freq.get(nums[right], 0) + 1

        while freq[nums[right]] > k:
            freq[nums[left]] -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

     return max_length



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna