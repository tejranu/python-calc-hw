import math

# create method to add, subtract, multiply, divide, square and square root

# add (return the value of the sum of num1 and num2)
def add_vals(num1, num2):
    int(num1)
    int(num2)
    return num1 + num2


# subtract (return the value of the difference of num1 and num2)
def subtract_vals(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    return num2 - num1


# multiply(return the value of the product of num1 and num2)
def multiply_vals(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    return num1 * num2


def divide_vals(num1, num2):
    float(num1)
    float(num2)

    return num1 / num2


def square_root_val(num):
    float(num)
    return math.sqrt(num)


def square_number_val(num):
    int(num)
    return num * num


class Calculator():
    value = 0

    def __init__(self):
        pass

    def add(self, num1, num2):
        self.value = add_vals(num1, num2)
        return self.value

    def subtract(self, num1, num2):
        self.value = subtract_vals(num1, num2)
        return self.value

    def multiply(self, num1, num2):
        self.value = multiply_vals(num1, num2)
        return self.value

    def divide(self, num1, num2):
        self.value = divide_vals(num1, num2)
        return self.value

    def square_root(self, num1):
        self.value = square_root_val(num1)
        return self.value

    def square_number(self, num1):
        self.value = square_number_val(num1)
        return self.value

