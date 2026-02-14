class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


a, b = map(int, input().split())
print(Rectangle(a, b).area())
