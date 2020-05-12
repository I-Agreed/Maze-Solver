class Grid:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.grid = [["." for i in range(self.h)] for i in range(self.w)]
    
    def set(self, x, y, char):
        self.grid[x][y] = char
    
    def get(self, x, y):
        return self.grid[x][y]
    
    def print(self):
        for i in range(self.w):
            line = ""
            for j in self.grid:
                line += j[i]
            print(line)
    
    def placeRect(self, x, y, w, h, char):
        for i in range(x, x+w+1):
            for j in range(y, y+h+1):
                self.set(i, j, char)
    
    def find(self, char):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == char:
                    return i,j
        return False