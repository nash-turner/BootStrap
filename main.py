import random


def read_file():
    length_file = open("data/Length.txt", "r")
    length = []
    for line in length_file:
        length.append(float(line.rstrip()))
    return length


def get_sample(size):
    sample = []
    for index in range(size):
        sample.append(random.choice(population))
    return sample


population = read_file()
sample = get_sample(100)


