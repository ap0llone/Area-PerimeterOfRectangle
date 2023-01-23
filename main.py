from colorama import init
init()
from colorama import Fore, Back, Style

print(Fore.RED)
sideA = int(input("Length: "))
sideB = int(input("Width: "))

print(Fore.BLUE)
area = sideA * sideB
perimeter = (sideA + sideB)*2

print(Fore.GREEN)
print("Perimeter: ", perimeter)
print("Area: ", area)












# print(Fore.RED)
# sideA = int(input("Длина: "))
# sideB = int(input("Ширина: "))

# area = sideA * sideB;
# perimeter = (sideA + sideB)*2

# print("Площадь прямоугольника: ", area)
# print("Периметр прямоугольника:",perimeter)