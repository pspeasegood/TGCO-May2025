import pprint
from collections import deque

class  RobotGrid(object):
    def __init__(self,x,y):
        self.x = abs(x)
        self.y = abs(y)
        self.printGrid()
        pass
    def isSafe(self, x, y):
        sum_of = x * y

        sum_of_digits = 0
        for digit in str(sum_of).replace("-","0"):
            sum_of_digits += abs(int(digit))
            #print(digit)
        
        #print(f'total for {self.x}, {self.y} is {sum_of_digits}')    
        return True if  sum_of_digits < 19  else False 

    def printGrid(self):
        self.x_array = [["" for i in range(-self.y,self.y)] for i in range(-self.x, self.x)]
        #print(self.x_array)
        for i in range(-self.x, self.x):
            for j in range(-self.y, self.y):
                self.x_array[i][j] = "0" if self.isSafe(i,j) else "X"
        # for row in self.x_array:
        #     #print(row)  
        

    def totalSafeSquares(self):
        if self.x_array[0][0] != "0":
            return 0
        
        num_rows = len(self.x_array)
        num_cols = len(self.x_array[0])

        visited = [[False for _ in range(num_cols)] for _ in range(num_rows)]

        queue = deque([(0,0)])
        visited[0][0] = True
        reachable_count = 1

        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        while queue:
            row, col = queue.popleft()

            for d_row, d_col in directions:
                next_row = row + d_row
                next_col = col + d_col

                if (
                    0 <= next_row < num_rows and
                    0 <= next_col < num_cols and
                    not visited[next_row][next_col] and
                    self.x_array[next_row][next_col] == "0"
                ):
                    visited[next_row][next_col] = True
                    queue.append((next_row, next_col))
                    reachable_count += 1
        return reachable_count
                

if __name__ == "__main__":
    x = 9999
    y = 9999
    rg = RobotGrid(x,y)
    total = 100
    #rg.printGrid()
    print(f"TOTAL SAFE SQUARES : {rg.totalSafeSquares()}")
    # for x in range(100):
    #     for y in range(100):
    #         print(f"{x}, {y}")
    #         print(rg.isSafe(x,y))       
