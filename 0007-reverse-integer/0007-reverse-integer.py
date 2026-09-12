class Solution:
    def reverse(self, x):

        sign = -1 if x < 0 else 1
        x = abs(x)

        ans = 0

        while x > 0:
            digit = x % 10
            x = x // 10

            ans = ans * 10 + digit

        ans = ans * sign

        if ans < -2**31 or ans > 2**31 - 1:
            return 0

        return ans
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna