
class Solution(object):
    def minSwaps(self, nums):
        n = len(nums)

        def digit_sum(x):
            return sum(int(digit) for digit in str(x))

        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))

        position = {num: i for i, num in enumerate(sorted_nums)}

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i]:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = position[nums[j]]
                cycle_size += 1

            if cycle_size > 1:
                swaps += cycle_size - 1

        return swaps


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna