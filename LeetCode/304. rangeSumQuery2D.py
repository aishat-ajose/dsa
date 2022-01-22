class NumMatrix:

    def __init__(self, matrix):
        matrix = matrix
        row = len(matrix)
        col = len(matrix[0])
        
        self.dp =  [[0 for _ in range(col)] for _ in range(row)]
        
        self.dp[0][0] = matrix[0][0]
        
        for r in range(1, row):
            self.dp[r][0] = matrix[r][0] + self.dp[r-1][0]
        
        for c in range(1, col):
            self.dp[0][c] = matrix[0][c] + self.dp[0][c-1]
            
        for r in range(1, row):
            for c in range(1, col):
                self.dp[r][c] = matrix[r][c] + self.dp[r][c-1] + self.dp[r-1][c] - self.dp[r-1][c-1]

        self.prefix_sum = self.dp

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int):
        if(row1 > 0 and col1 > 0):
            return self.dp[row2][col2]  - self.dp[row1 -1][col2] - self.dp[row2][col1 -1] +  self.dp[row1 -1][col1 -1]
        elif(row1 > 0):
            return self.dp[row2][col2] - self.dp[row1 -1][col2]
        elif(col1 > 0):
            return self.dp[row2][col2] - self.dp[row2][col1 -1]
        else: 
            return self.dp[row2][col2]
        