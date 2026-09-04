class Solution(object):
    def plusOne(self, digits):
        num = ''.join(map(str,digits))
        new = int(num)+1
        arr = [int(i) for i in str(new)]
        return arr 

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna