from random import random

def GetSample(number_list, sample_size):
    random_values = random.sample(number_list, k = sample_size)
    return random_values