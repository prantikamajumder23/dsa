class Solution(object):
    def singleNumber(self, nums):
        ans=0
        for i in nums:
            ans = ans ^ i 
        return ans 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna