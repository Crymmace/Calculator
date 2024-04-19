import random
import time
random.seed(time.time)


def addition(*args):
    sum_ = 0
    for a in args[0]:
        sum_ += a
    return sum_


def subtraction(*args):
    difference = 0
    for a in args[0]:
        difference -= a
    return difference


def multiplication(*args):
    product = 1
    for a in args[0]:
        product *= a
    return product


def division(*args):
    quotient = 1
    if len(args[0]) > 2:
        for a in args[0]:
            quotient = a / quotient
            print(a)
            print(quotient)
        return quotient
    else:
        quotient = args[0][0] / args[0][1]
        return quotient


def create_num(num):
    num = "".join(num)
    num = float(num)
    return num


def get_zero_divide_message():
    with open("dont_divide_by_zero.txt", "r") as file:
        lines = file.readlines()
        index = random.randint(0, len(lines) - 1)
        return lines[index]


# Todo: Fix Math for more than 2 numbers