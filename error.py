"""Класс(ы) исключений с выводом подробной информации."""

class RectangleError(Exception):

    def __init__(self, message):
        pass


class InvalidSizeError(RectangleError):

    def __init__(self, attribute, value):
        self.attribute = attribute
        self.value = value

    def __str__(self):
        return f"Invalid value detected: {self.attribute} = {self.value}"

