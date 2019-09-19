class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def coordinates(self):
        print(f'Координаты: x {self.x}, y {self.y}')

    def __repr__(self):
        return

my_point = Point(5,3)

my_point.coordinates()

