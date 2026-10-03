class Solution(object):
    def longestValidParentheses(self, s):
     stack=[-1]
     m_len = 0
     for i in range(len(s)):
        if s[i]=='(':
            stack.append(i)

        else:
            stack.pop()

            if not stack:
                stack.append(i)
            else:
                m_len=max(m_len,i-stack[-1])
     return m_len

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna