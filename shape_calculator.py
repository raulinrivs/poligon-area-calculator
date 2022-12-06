class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width <= 50 and self.height <= 50:
            picture = ''
            for x in range(self.height):
                for y in range(self.width):
                    picture += '*'
                picture += '\n'
            print(picture)
            return picture
        else:
            return 'Too big for picture.'

    def get_amount_inside(self, shape):
        new_shape_area = shape.get_area()
        shape_area = self.get_area()
        return shape_area // new_shape_area


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def __str__(self):
        return f'Square(side={self.side})'

    def set_side(self, side):
        self.side = side
        self.height = side
        self.width = side

    def set_width(self, width):
        self.width = width
        self.height = width
        self.set_side(width)

    def set_height(self, height):
        self.width = height
        self.height = height
        self.set_side(height)
