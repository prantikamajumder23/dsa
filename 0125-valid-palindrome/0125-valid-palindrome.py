class Solution(object):
    def isPalindrome(self, s):
        clean = ""

        for char in s:
            if char.isalnum():
                clean += char.lower()

        return clean == clean[::-1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna