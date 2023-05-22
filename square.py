class Square:

    def __init__(self, x, y, side, color):
        self.color = color
        self.side = side
        self.x = x
        self.y = y
    
    def draw(self, canvas):
        
        canvas.data[self.x: self.x + self.side, self.y: self.y + self.side] = self.color