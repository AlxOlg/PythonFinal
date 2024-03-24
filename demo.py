"""
Демонстрация работы класса Rectangle.
Создаются два прямоугольника, вычисляются периметры и площади, 
прямоугольники сравниваются, производится их сложение и вычитание.
Результат выводится в консоль.
"""

from rectangle import Rectangle


def out_info(name: str, obj: Rectangle):
    print()
    print(name)
    if obj:
        print(f"length = {obj.length}, width = {obj.width}")
        print(f"perimeter = {obj.perimeter()}")
        print(f"area = {obj.area()}")
    else:
        print("does not exist")


def out_demo(rectangle1, rectangle2):
    out_info('First rectangle:', rectangle1)
    out_info('Second rectangle:', rectangle2)

    print()
    if rectangle1 > rectangle2:
        print("First rectangle > Second rectangle")
    if rectangle1 < rectangle2:
        print("First rectangle < Second rectangle")
    if rectangle1 == rectangle2:
        print("First rectangle == Second rectangle")

    rectangle3 = rectangle1 + rectangle2
    out_info('Add rectangle:', rectangle3)
            
    rectangle4 = rectangle1 - rectangle2
    out_info('Sub rectangle:', rectangle4)


if __name__ == '__main__':
    rectangle1 = Rectangle(10, 6)
    rectangle2 = Rectangle(8, 4)
    out_demo(rectangle1, rectangle2)
