"""Output"""
import math


def main():
    """Pre"""
    seconds = int(input())
    minutes = seconds//60
    seconds = seconds % 60
    hours = minutes//60
    minutes = minutes % 60
    days = hours//24
    hours = hours % 24
    print("%s %s %s %s" % (days, hours, minutes, seconds))


main()
