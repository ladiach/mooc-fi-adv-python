# Write your solution here!
class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def __str__(self):
        return f"rectangle {self.width}x{self.height}"

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    
    def __init__(self, height:int):
        super().__init__(height, height)
    
    def __str__(self):
        return f"square {self.height}x{self.height}"