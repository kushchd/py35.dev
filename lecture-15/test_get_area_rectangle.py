#
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

class TestGetAreaRectangle:
    def test_normal_case(self):
        rectangle = Rectangle(2, 3)
        assert rectangle.get_area() == 6, "incorrect area"

    def test_negative_case(self):
        rectangle = Rectangle(-1, 2)
        assert rectangle.get_area() == -1, "incorrect negative output"
