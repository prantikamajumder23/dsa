class Solution(object):
    def minInsertions(self, s):
        count = 0
        result = 0
        for i in s :
            if i =='(':
                if count %2 ==1:
                    result +=1
                    count -=1 
                count +=2   
            else:
                count -=1
                if count <0:
                    result +=1
                    count = 1
        return result + count 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna