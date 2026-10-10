class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        k = k1 + k2
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]

        if sum(diffs) <= k:
            return 0

        left, right = 0, max(diffs)

        while left < right:
            mid = (left + right) // 2
            ops = sum(max(0, d - mid) for d in diffs)

            if ops <= k:
                right = mid
            else:
                left = mid + 1

        ans = 0
        remaining = k

        for d in diffs:
            if d > left:
                remaining -= d - left
                d = left
            ans += d * d

        
        ans -= remaining * (2 * left - 1)

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna