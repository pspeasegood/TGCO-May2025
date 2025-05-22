import pprint
class  RobotGrid(object):
    def __init__(self):
        pass
    def isSafe(self, x, y):
        sum_of = x * y

        sum_of_digits = 0
        for digit in str(sum_of):
            sum_of_digits += int(digit)
            print(digit)
        
        print(f'total for {x}, {y} is {sum_of_digits}')    
        return "O" if  sum_of_digits < 19  else "X" 

    def printGrid(self, x, y):
        x_array = [["" for i in range(y)] for i in range(x)]
        print(x_array)
        for i in range(x):
            for j in range(y):
                x_array[i][j] = self.isSafe(i,j)
        for row in x_array:
            print(row)        
                

if __name__ == "__main__":
    rg = RobotGrid()
    total = 100
    rg.printGrid(999,35)
    # for x in range(100):
    #     for y in range(100):
    #         print(f"{x}, {y}")
    #         print(rg.isSafe(x,y))       