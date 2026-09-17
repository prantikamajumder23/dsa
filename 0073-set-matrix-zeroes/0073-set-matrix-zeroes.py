class Solution(object):
    def setZeroes(self, matrix):
        zrow=[]
        zcol=[]
        for i in range(len(matrix)):
         for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
               zrow.append(i)
               zcol.append(j)
        for i in zrow:
            for j in range(len(matrix[0])):
                matrix[i][j]=0
        for j in zcol:
            for i in range(len(matrix)):
                matrix[i][j]=0


        return matrix 
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna