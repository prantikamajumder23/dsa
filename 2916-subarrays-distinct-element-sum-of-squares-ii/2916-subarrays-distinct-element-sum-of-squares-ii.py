class Solution(object):
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)

        total = [0] * (4 * n)
        square = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def update(node, start, end, left, right):
            if left <= start and end <= right:
                length = end - start + 1

                square[node] += 2 * total[node] + length
                total[node] += length
                lazy[node] += 1
                return

            mid = (start + end) // 2

            if lazy[node]:
                val = lazy[node]

                for child, l, r in (
                    (node * 2, start, mid),
                    (node * 2 + 1, mid + 1, end)
                ):
                    length = r - l + 1
                    square[child] += (
                        2 * val * total[child]
                        + val * val * length
                    )
                    total[child] += val * length
                    lazy[child] += val

                lazy[node] = 0

            if left <= mid:
                update(node * 2, start, mid, left, right)

            if right > mid:
                update(node * 2 + 1, mid + 1, end, left, right)

            total[node] = total[node * 2] + total[node * 2 + 1]
            square[node] = square[node * 2] + square[node * 2 + 1]

        last_seen = {}
        answer = 0

        for i, num in enumerate(nums):
            prev = last_seen.get(num, -1)

            update(1, 0, n - 1, prev + 1, i)

            answer = (answer + square[1]) % MOD
            last_seen[num] = i

        return answer

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna