class Solution(object):
    def longestCommonPrefix(self,strs):
     prefix = strs[0]

     for word in strs[1:]:
         while not word.startswith(prefix):
            prefix = prefix[:-1]

            if prefix == "":
                return ""

     return prefix
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna