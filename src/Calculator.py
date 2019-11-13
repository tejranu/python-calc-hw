import math
from src.statistics.Statistics import Statistics

# create method to add, subtract, multiply, divide, square and square root
stat = Statistics()


def population_mean(number_list):
    return stat.population_mean(number_list)


def median(number_list):
    return stat.median(number_list)


def pop_standard_deviation(number_list):
    return stat.pop_standard_deviation(number_list)


def mode(number_list):
    return stat.mode(number_list)


def variance_pop_proportion(number_list):
    return stat.variance_pop_proportion(number_list)


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
    return num2 / num1


def square_root_val(num):
    float(num)
    return math.sqrt(num)


def square_number_val(num):
    int(num)
    return num * num


class Calculator:
    value = 0

    def __init__(self):
        pass

    def population_mean(self, number_list):
        self.value = population_mean(number_list)
        return self.value

    def median(self, number_list):
        self.value = median(number_list)
        return self.value

    def pop_standard_deviation(self, number_list):
        self.value = pop_standard_deviation(number_list)
        return self.value

    def mode(self, number_list):
        self.value = mode(number_list)
        return self.value

    def variance_pop_proportion(self, number_list):
        self.value = variance_pop_proportion(number_list)
        return self.value

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
        return round(float(self.value), 8)

    def square_root(self, num1):
        self.value = square_root_val(num1)
        return self.value

    def square_number(self, num1):
        self.value = square_number_val(num1)
        return self.value

