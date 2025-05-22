import pprint
class  RobotGrid(object):
    def __init__(self,x,y):
        self.x = abs(x)
        self.y = abs(y)
        pass
    def isSafe(self, x, y):
        sum_of = x * y

        sum_of_digits = 0
        for digit in str(sum_of):
            sum_of_digits += abs(int(digit))
            print(digit)
        
        print(f'total for {self.x}, {self.y} is {sum_of_digits}')    
        return True if  sum_of_digits < 19  else False 

    def printGrid(self):
        x_array = [["" for i in range(self.y)] for i in range(self.x)]
        print(x_array)
        for i in range(self.x):
            for j in range(self.y):
                x_array[i][j] = "0" if self.isSafe(i,j) else "X"
        for row in x_array:
            print(row)        
                

if __name__ == "__main__":
    x = -999
    y = 35
    rg = RobotGrid(x,y)
    total = 100
    rg.printGrid()
    # for x in range(100):
    #     for y in range(100):
    #         print(f"{x}, {y}")
    #         print(rg.isSafe(x,y))       
