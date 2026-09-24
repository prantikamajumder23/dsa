class Solution:
    def find132pattern(self, nums):
        stack = []
        third = float('-inf')

        for i in range(len(nums) - 1, -1, -1):

            
            if nums[i] < third:
                return True

           
            while stack and nums[i] > stack[-1]:
                third = stack.pop()

            stack.append(nums[i])

        return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna