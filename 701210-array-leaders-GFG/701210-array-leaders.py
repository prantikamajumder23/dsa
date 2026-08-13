class Solution:
    def leaders(self, arr):
        result = []
        n = len(arr)
        maxright = arr[-1]
        result.append(maxright)
        for i in range (n-2,-1,-1):
            if  arr[i]>= maxright:
                maxright=arr[i]
                result.append(maxright)
        result.reverse()
        return result 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna