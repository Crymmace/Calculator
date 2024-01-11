import random
import time
random.seed(time.time)

def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


def create_num(num):
    x = "".join(num)
    x = float(x)
    return x


def get_zero_divide_message():
    with open("dont_divide_by_zero.txt", "r") as file:
        lines = file.readlines()
        index = random.randint(0, len(lines) - 1)
        return lines[index]
