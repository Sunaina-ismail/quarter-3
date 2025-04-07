# Implement an 'eraser' on a canvas.
# The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. We then create an eraser rectangle which, when dragged around the canvas, sets all of the rectangles it is in contact with to white.


import tkinter as tk

class EraserCanvas:
    def __init__(self, root, rows=10, cols=10, cell_size=40):
        self.root = root
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.eraser_size = cell_size * 2
        
        self.canvas = tk.Canvas(root, width=cols * cell_size, height=rows * cell_size, bg="white")
        self.canvas.pack()
        
        self.cells = [] 
        self.create_grid()
        
        
        self.eraser = self.canvas.create_rectangle(0, 0, self.eraser_size, self.eraser_size, fill="gray", outline="black")
        
        self.canvas.bind("<B1-Motion>", self.move_eraser)
    
    def create_grid(self):
        for row in range(self.rows):
            row_cells = []
            for col in range(self.cols):
                x1, y1 = col * self.cell_size, row * self.cell_size
                x2, y2 = x1 + self.cell_size, y1 + self.cell_size
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="black")
                row_cells.append(rect)
            self.cells.append(row_cells)
    
    def move_eraser(self, event):
        x1, y1 = event.x - self.eraser_size // 2, event.y - self.eraser_size // 2
        x2, y2 = x1 + self.eraser_size, y1 + self.eraser_size
        self.canvas.coords(self.eraser, x1, y1, x2, y2)
        
   
        for row in self.cells:
            for rect in row:
                x1, y1, x2, y2 = self.canvas.coords(rect)
                eraser_coords = self.canvas.coords(self.eraser)
                if self.overlaps(x1, y1, x2, y2, *eraser_coords):
                    self.canvas.itemconfig(rect, fill="white")
    
    def overlaps(self, x1, y1, x2, y2, ex1, ey1, ex2, ey2):
        return not (x2 < ex1 or x1 > ex2 or y2 < ey1 or y1 > ey2)


root = tk.Tk()
root.title("Canvas Eraser Tool")
EraserCanvas(root)
root.mainloop()
