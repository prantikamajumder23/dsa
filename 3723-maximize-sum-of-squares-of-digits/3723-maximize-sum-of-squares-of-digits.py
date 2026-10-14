class Solution(object):
    def maxSumOfSquares(self, num, sum):
         if num * 9 < sum:
            return ""

         k = sum // 9
         s = sum % 9

         ans = "9" * k

         if s > 0:
            ans += str(s)

         ans += "0" * (num - len(ans))

         return ans
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna