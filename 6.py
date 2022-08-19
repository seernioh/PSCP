"""Output"""
import math


def main():
    """Pre"""
    number_x = int(input())
    number_y = int(input())
    number_z = int(input())
    print(number_x+1)
    print(7*number_y**3+2*number_y**2-31*number_y+1)
    print(0-number_z)
    print((number_x+number_y)*(number_x-number_y))
    print((number_y-math.sqrt(number_y**2-4*number_x*number_z))/2*number_x)


main()
