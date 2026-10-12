class Solution(object):
    def maxSum(self, nums, k):
        MOD = 10**9 + 7 
        count = [0] * 31
        for num in nums:
            for i in range(31):
                if num >> i & 1 :
                    count[i] += 1

        ans = 0 
        for _ in range(k):
            num = 0 
            for i in range (31):
                 if count[i] > 0:
                    num |= (1 << i)
                    count[i] -= 1
            ans = (ans+num*num) % MOD 
        return ans 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna