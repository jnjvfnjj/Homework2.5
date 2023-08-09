class Shape:
    def draw():
        return "Рисуем фигуру"
    
class Circle(Shape):
    def do(self):
        return "пишется круг"
    
class Rectangle(Shape):
    def do(self):
        return "пишется прямоугольник"
    
def doing(Shape):
    return Shape.do()


circle = Circle()
rectangle = Rectangle()
print(doing(circle))
print(doing(rectangle))







class Counter:
    def __init__(self):
        self.value = 0

    def increment(self, value):
        self.value += value

    def get_value(self):
        return self.value

counter = Counter()
print(counter.get_value())
counter.increment(10)
print(counter.get_value())
counter.increment(30)
print(counter.get_value())
