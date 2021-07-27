import math


class Square:
    def __init__(self, length) -> None:
        self.length = length


class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius


class AreaCalculator:
    def __init__(self, shapes) -> None:
        self.shapes = shapes

    def sum(self):
        area = list()
        for shape in self.shapes:
            if type(shape).__name__ == 'Square':
                area.append(pow(shape.length, 2))
            elif type(shape).__name__ == 'Circle':
                area.append(math.pi * pow(shape.radius, 2))
        return sum(area)

    def output(self):
        return "Sum of the areas of provided shapes: " + str(self.sum())


def main():
    c1 = Circle(2)
    s1 = Square(5)
    s2 = Square(6)
    shapes = [c1, s1, s2]
    areas = AreaCalculator(shapes)
    print(areas.output())


if __name__ == '__main__':
    main()
