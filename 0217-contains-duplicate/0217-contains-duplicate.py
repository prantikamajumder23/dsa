class Solution(object):
    def containsDuplicate(self, nums):
      n = len(nums)
      nums.sort()
      for i in range(n-1):
         if nums[i]==nums[i+1]:
                return True

      return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna