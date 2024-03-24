"""Скрипт для запуска из командной строки с передачей параметров."""

import argparse

from demo import out_demo
from rectangle import Rectangle


def out_parser():
    parser = argparse.ArgumentParser(description='Takes parameters for two rectangles')
    parser.add_argument('-l1', '--length1', type=float, help='Length of the first rectangle')
    parser.add_argument('-w1', '--width1', type=float, help='Width of the first rectangle')
    parser.add_argument('-l2', '--length2', type=float, help='Length of the second rectangle')
    parser.add_argument('-w2', '--width2', type=float, help='Width of the second rectangle')
    return parser.parse_args()


if __name__ == '__main__':
    args = out_parser()
    rectangle1 = Rectangle(args.length1, args.width1)
    rectangle2 = Rectangle(args.length2, args.width2)
    out_demo(rectangle1, rectangle2)
