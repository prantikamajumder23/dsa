class Solution:
    def getRow(self, rowIndex):
        row = [1] * (rowIndex + 1)

        for i in range(1, rowIndex):
            for j in range(i, 0, -1):
                row[j] += row[j - 1]

        return row

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna