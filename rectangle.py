"""
Класс Rectangle.
Принимает длину и ширину,
возвращает периметр и площадь,
производится сложение и вычитание (периметров),
сравнение прямоугольников по площади.
Производится логирование ошибок и информации работы класса.
"""

import logging

from error import InvalidSizeError


FORMAT = '{asctime} {levelname} {filename} {funcName} {lineno} {message}'
logging.basicConfig(level=logging.INFO, filename='mylog.log', filemode='w', encoding='utf-8', format = FORMAT, style = '{')
logger = logging.getLogger(__name__)


class Rectangle:
    __slots__ = ['_length', '_width']

    def __init__(self, length, width=None):
        logger.info(f"Arguments received: {length=}, {width=}")
        try:
            if length <= 0:
                raise InvalidSizeError("length", length)
            if width is not None and width <= 0:
                raise InvalidSizeError("width", width)
        except Exception:
            logger.critical("Argument error.", exc_info=True)
            raise

        self._length = length
        self._width = width if width else length
        logger.info("Rectangle created.")

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        try:
            logger.info(f"Received new length value: {value}")
            if value <= 0:
                raise InvalidSizeError("length", value)
        except Exception:
            logger.critical("Value error.", exc_info=True)
            raise
        self._length = value
        logger.info(f"Set new length value: {value}")

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        logger.info(f"Received new width value: {value}")
        try:
            if value <= 0:
                raise InvalidSizeError("width", value)
        except Exception:
            logger.critical("Value error.", exc_info=True)
            raise
        self._width = value
        logger.info(f"Set new width value: {value}")

    def perimeter(self):
        new_perimeter = 2 * (self._length + self._width)
        logger.info(f"Perimeter calculation: {new_perimeter}")
        return new_perimeter

    def area(self):
        new_area = self._length * self._width
        logger.info(f"Area calculation: {new_area}")
        return new_area
    
    def __add__(self, other):
        try:
            new_perimeter = self.perimeter() + other.perimeter()
            logger.info(f"Addition completed. {new_perimeter=}")
            return Rectangle.from_perimeter(new_perimeter)
        except Exception:
            logging.critical("Addition error.", exc_info=True)

    def __sub__(self, other):
        try:
            new_perimeter = abs(self.perimeter() - other.perimeter())
            logger.info(f"Subtraction completed. {new_perimeter=}")
            return Rectangle.from_perimeter(new_perimeter)
        except Exception:
            logging.critical("Subtraction error.", exc_info=True)
        
    @classmethod
    def from_perimeter(cls, perimeter):
        return cls(perimeter / 4)

    def __eq__(self, other):
        return self.area() == other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __ne__(self, other):
        return self.area() != other.area()
