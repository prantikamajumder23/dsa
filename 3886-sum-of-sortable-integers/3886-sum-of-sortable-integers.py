class Solution(object):
    def sortableIntegers(self, nums):
        n = len(nums)

        prefMax = [0] * (n + 1)
        suffMin = [float('inf')] * (n + 1)
        prefDrop = [0] * (n + 1)

        for i in range(n):
            prefMax[i + 1] = max(prefMax[i], nums[i])
            prefDrop[i + 1] = prefDrop[i]

            if i > 0 and nums[i - 1] > nums[i]:
                prefDrop[i + 1] += 1

        for i in range(n - 1, -1, -1):
            suffMin[i] = min(nums[i], suffMin[i + 1])

        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True

            for start in range(0, n, k):
                end = start + k - 1

                drops = prefDrop[end + 1] - prefDrop[start + 1]

                if nums[end] > nums[start]:
                    drops += 1

                if drops > 1:
                    valid = False
                    break

                if start > 0 and prefMax[start] > suffMin[start]:
                    valid = False
                    break

            if valid:
                ans += k

        return ans
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna