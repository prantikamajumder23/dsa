class Solution(object):
    def generateParenthesis(self, n):
         ans = []

         def backtrack(s, open, close):
            if len(s) == 2 * n:
                ans.append(s)
                return

            if open < n:
                backtrack(s + "(", open + 1, close)

            if close < open:
                backtrack(s + ")", open, close + 1)

         backtrack("", 0, 0)
         return ans 
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna