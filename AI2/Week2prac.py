from hashlib import new
from matplotlib import pyplot as plt
import random
import numpy as np

N = 10
P = 50


class individual:
    gene = []
    fitness = 0


population = []

for x in range(0, P):
    tempgene = []
    for x in range(0, N):
        tempgene.append(random.randint(0, 1))
    newind = individual()
    newind.gene = tempgene.copy()
    population.append(newind)


def test_func(individual):
    fitness = 0
    for x in range(0, N):
        if individual.gene[x] == 1:
            fitness += 1


for i in range(0, P):
    offarray = []
    parent1 = random.randint(0, P - 1)
    off1 = population[parent1]
    parent2 = random.randint(0, P - 1)
    off2 = population[parent2]

    if off1.fitness > off2.fitness:
        offarray.append(off1)

    else:
        offarray.append(off2)
    if offarray.fitness()

print(individual.fitness)
